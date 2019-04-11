from src.data_processing.classifier import STATE_CLASSIFIER_SHIELD, STATE_CLASSIFIER_DODGE

ESCAPE_FRAME_COUNT = 10 # number of frames to record for when a player drops shield


ESCAPE_STATE_ROLL = 20
ESCAPE_STATE_WAVEDASH = 21
ESCAPE_STATE_DASH = 22
ESCAPE_STATE_JUMP = 23
ESCAPE_STATE_ATTACK = 24
ESCAPE_STATE_MISC = 25

ESCAPE_STATE_NAMES = {
    ESCAPE_STATE_ROLL: "roll",
    ESCAPE_STATE_WAVEDASH: "wavedash",
    ESCAPE_STATE_DASH: "dash",
    ESCAPE_STATE_JUMP:"jump",
    ESCAPE_STATE_ATTACK: "attack",
    ESCAPE_STATE_MISC: "misc"
}


def getEscapeOutOfShieldData(game_stats):
    """

    :param game_stats:
    :return: [[], []] # player 1, player 2
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
    for k in range(ESCAPE_FRAME_COUNT):
        escape_state_list.append(game_stats['state_data'][frame + k][(player + 1) % 2])
    return classifyEscapeStateList(escape_state_list)

def classifyEscapeStateList(escape_state_list):
    """Classify a list of states into escape-specific states, like wavedash, roll, attack"""
    if escape_state_list.count(STATE_CLASSIFIER_DODGE) == ESCAPE_FRAME_COUNT:
        return ESCAPE_STATE_ROLL
    else:
        return ESCAPE_STATE_MISC

