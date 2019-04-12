from src.data_processing.classifier import STATE_CLASSIFIER_SHIELD, STATE_CLASSIFIER_DODGE, \
    STATE_CLASSIFIER_MOVING_GROUND, STATE_CLASSIFIER_DOWNED_GROUND, STATE_CLASSIFIER_DOWNED_AIR, \
    STATE_CLASSIFIER_ATTACK_GROUND, STATE_CLASSIFIER_ATTACK_AIR, STATE_CLASSIFIER_NEUTRAL, STATE_CLASSIFIER_MOVING_AIR

ESCAPE_FRAME_COUNT = 10 # number of frames to record state for when a player drops shield
ESCAPE_PUNISH_FRAMES_COUNT = 30 # number of frames to check whether a player has been punished for a particular OOS option


ESCAPE_STATE_ROLL = 20
ESCAPE_STATE_WAVEDASH = 21
ESCAPE_STATE_DASH = 22
ESCAPE_STATE_JUMP = 23
ESCAPE_STATE_ATTACK = 24
ESCAPE_STATE_ATTACKED = 25
ESCAPE_STATE_TRADE = 26
ESCAPE_STATE_MISC = 27

ESCAPE_STATE_NAMES = {
    ESCAPE_STATE_ROLL: "roll",
    ESCAPE_STATE_WAVEDASH: "wavedash",
    ESCAPE_STATE_DASH: "dash",
    ESCAPE_STATE_JUMP:"jump",
    ESCAPE_STATE_ATTACK: "attack",
    ESCAPE_STATE_ATTACKED: "attacked",
    ESCAPE_STATE_TRADE: "trade",
    ESCAPE_STATE_MISC: "misc"
}


def getEscapeOutOfShieldData(game_stats):
    """

    :param game_stats:
    :return: [[[oos_state, damage_taken]], []] # player 1, player 2
    """
    shield_escape_data = [[], []]
    for i, frame in enumerate(game_stats['game'].frames):
        for j, port in enumerate(frame.ports):
            other_player_state = game_stats['state_data'][i][(j+1)%2]
            if i == 0:
                previous_other_player_state = None
            else:
                previous_other_player_state = game_stats['state_data'][i-1][(j+1)%2]
            if previous_other_player_state == STATE_CLASSIFIER_SHIELD:
                if other_player_state == STATE_CLASSIFIER_SHIELD:
                    pass
                else:
                    escape_state = getEscapeState(game_stats, i, j)
                    shield_escape_data[(i+1)%2].append(escape_state)

    return shield_escape_data


def getEscapeState(game_stats, frame, player):
    escape_state_list = []
    other_player = (player + 1) % 2
    start_damage = game_stats['game'].frames[frame].ports[other_player].leader.post.damage
    for k in range(ESCAPE_FRAME_COUNT):
        escape_state_list.append(game_stats['state_data'][frame + k][other_player])
    end_damage = game_stats['game'].frames[frame+ESCAPE_PUNISH_FRAMES_COUNT].ports[other_player].leader.post.damage
    return [classifyEscapeStateList(escape_state_list), end_damage-start_damage]

def classifyEscapeStateList(escape_state_list):
    """Classify a list of states into escape-specific states, like wavedash, roll, attack"""
    # If they are dodging the whole time, its a roll
    if escape_state_list.count(STATE_CLASSIFIER_DODGE) == ESCAPE_FRAME_COUNT:
        return ESCAPE_STATE_ROLL
    # if they attack, it could be a trade or an attack out of shield
    elif escape_state_list.count(STATE_CLASSIFIER_ATTACK_GROUND) + \
         escape_state_list.count(STATE_CLASSIFIER_ATTACK_AIR) > 0:
        if escape_state_list.count(STATE_CLASSIFIER_DOWNED_GROUND) + \
         escape_state_list.count(STATE_CLASSIFIER_DOWNED_AIR) > 0:
            # If they attack and then also get hit, it's a trade
            return ESCAPE_STATE_TRADE
        else:
            # Otherwise its an attack OOS
            return ESCAPE_STATE_ATTACK
    elif escape_state_list.count(STATE_CLASSIFIER_DOWNED_GROUND) + \
         escape_state_list.count(STATE_CLASSIFIER_DOWNED_AIR) > 0:
        # If they get hit, then they were attacked out of shield
        return ESCAPE_STATE_ATTACKED
    elif escape_state_list[0] == STATE_CLASSIFIER_MOVING_GROUND and escape_state_list.count(STATE_CLASSIFIER_DODGE) >= 1:
        # if they jumpsquat and then airdodge, thats a wavedash
        return ESCAPE_STATE_WAVEDASH
    # If they spent half the time moving on ground or standing, its a dash
    elif escape_state_list.count(STATE_CLASSIFIER_MOVING_GROUND) + \
         escape_state_list.count(STATE_CLASSIFIER_NEUTRAL) > ESCAPE_FRAME_COUNT//2:
        return ESCAPE_STATE_DASH
    elif escape_state_list.count(STATE_CLASSIFIER_MOVING_AIR) > 0:
        return ESCAPE_STATE_JUMP
    else:
        # Otherwise Idk what it is, fill in more conditions to reduce misc classifys
        return ESCAPE_STATE_MISC

def printEscapeShieldData(game_stats):
    output = ""
    for i, player_shield in enumerate(game_stats['escape_oos']):
        output += "Player {} OOS Options  :\n".format(i + 1)
        output += "Total OOS Situations    : {}\n".format(len(game_stats['escape_oos'][i]))
        output += "Total OOS punished      : {}\n".format(len([o for o in game_stats['escape_oos'][i] if o[1] > 0]))
        for oos in game_stats['escape_oos'][i]:
            if oos[1] > 0: punished = True
            else: punished = False
            output += ESCAPE_STATE_NAMES[oos[0]] + ": Punished: {}".format(punished) + "\n"
    return output
