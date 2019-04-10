import slippi

from src.data_processing.classifier import STATE_CLASSIFIER_ATTACK_GROUND, STATE_CLASSIFIER_ATTACK_AIR, \
    STATE_CLASSIFIER_DOWNED_GROUND, STATE_CLASSIFIER_DOWNED_AIR, STATE_CLASSIFIER_SHIELD, STATE_CLASSIFIER_NEUTRAL, \
    STATE_CLASSIFIER_MOVING_GROUND, STATE_CLASSIFIER_DEAD

COMBO_FRAME_THRESHOLD = 60 # Number of frames the defender must be in a grounded, 'active' state before a combo 'ends'
COMBO_PERCENT_THRESHOLD = 5 # Ignore any combos less than this percent
COMBO_ATTACKS_THRESHOLD = 2 # Ignore any combos consisting of less than this number of attacks
ATTACKS_PERCENT_THRESHOLD = 4 # Ignore any attacks less than this percent (filters out lasers, jabs etc)


class Combo:
    def __init__(self, start_frame):
        self.start_frame = start_frame
        self.end_frame = start_frame
        self.attacks = []
        self.percent_start = 0
        self.percent_end = 0
        self.percent_total = 0
        self.kill = False
        self.finished = False
        self.combo_end_tally = 0

    def __str__(self):
        attack_string = "\n"
        for attack in self.attacks:
            attack_string += "  {}\n".format(attack)
        return "Percent: {}\nAttacks: {}".format(round(self.percent_total), attack_string)

class Attack:
    def __init__(self, name, start_frame):
        self.name = name
        self.start_frame = start_frame
        self.end_frame = start_frame
        self.percent = 0

    def __str__(self):
        attack_name = slippi.id.ActionState(self.name).name
        return "{}:{}%".format(attack_name, round(self.percent))

def getComboData(game_stats):
    """
    Analyze framedata/state_data and mark combos

    :param game_stats: game_stats object from stats.py
    :return: combo data
    """
    # TODO: attack state name isn't always correct, probably due to projectiles, aerials, or delayed moves
    # TODO: ex. a missile hit would read the state of samus as walking or jumping at the time the missile hits
    # TODO: need to have a getLastAttack function and classify combos based on downed state only
    combo_data = [[], []] # player 1, player 2
    player_1_last_data = None
    player_2_last_data = None
    player_1_free = True
    player_2_free = True
    for i, frame in enumerate(game_stats['game'].frames):
        player_1_data = None
        player_1_state = None
        player_2_data = None
        player_2_state = None
        for j, port in enumerate(frame.ports):
            if port is not None:
                data = port.leader
                state = game_stats['state_data'][i][j]
                if player_1_data is None:
                    player_1_data = data
                    player_1_state = state
                else:
                    player_2_data = data
                    player_2_state = state
        if i == 0: pass
        else:
            # identify attacks that are part of a combo
            # PLAYER 1 COMBOS PLAYER 2
            if player_1_state == STATE_CLASSIFIER_ATTACK_GROUND or STATE_CLASSIFIER_ATTACK_AIR:
                if player_2_state == STATE_CLASSIFIER_DOWNED_GROUND or STATE_CLASSIFIER_DOWNED_AIR or STATE_CLASSIFIER_SHIELD:
                    # the attack hit
                    name = player_1_data.post.state
                    if name == player_1_last_data.post.state:
                        try:
                            if (i-combo_data[0][-1].attacks[-1].end_frame) <= 2:
                                combo_data[0][-1].attacks[-1].end_frame += 1
                        except IndexError:
                            pass # Late hit move, disregard
                        pass # only add a move on the first frame it appears
                    attack = Attack(name, i)
                    try: # ensure there is a combo to add the move to
                        last_combo = combo_data[0][-1]
                        if last_combo.finished:
                            combo = Combo(i)
                            combo_data[0].append(combo)
                    except IndexError:
                        combo = Combo(i)
                        combo_data[0].append(combo)
                    combo_data[0][-1].attacks.append(attack)
                else:
                    pass # The attack didn't hit

            # UPDATE PLAYER 1 COMBOS
            if player_2_state == STATE_CLASSIFIER_NEUTRAL or player_2_state == STATE_CLASSIFIER_MOVING_GROUND:
                # player 2 has escaped the combo, start the frame tally
                player_2_free = True
            elif player_2_state == STATE_CLASSIFIER_DOWNED_GROUND or player_2_state == STATE_CLASSIFIER_DOWNED_AIR:
                # player 2 has gotten hit again, resume combo
                player_2_free = False
                try:
                    last_combo = combo_data[0][-1]
                    if not last_combo.finished:
                        last_combo.combo_end_tally = 0
                except IndexError:
                    pass
            elif player_2_state == STATE_CLASSIFIER_DEAD:
                # End the last combo due to leading to a kill
                player_2_free = True
                try:
                    last_combo = combo_data[0][-1]
                    if not last_combo.finished:
                        last_combo = combo_data[0][-1]
                        last_combo.finished = True
                        last_combo.kill = True
                        last_combo.end_frame = i
                except IndexError:
                    pass
            else:
                if player_2_free:
                    try:
                        last_combo = combo_data[0][-1]
                        if not last_combo.finished:
                            last_combo.combo_end_tally += 1
                            if last_combo.combo_end_tally >= COMBO_FRAME_THRESHOLD:
                                last_combo.finished = True
                                last_combo.end_frame = i
                    except IndexError:
                        pass

            # PLAYER 2 COMBOS PLAYER 1
            if player_2_state == STATE_CLASSIFIER_ATTACK_GROUND or STATE_CLASSIFIER_ATTACK_AIR:
                if player_1_state == STATE_CLASSIFIER_DOWNED_GROUND or STATE_CLASSIFIER_DOWNED_AIR or STATE_CLASSIFIER_SHIELD:
                    # the attack hit
                    name = player_2_data.post.state
                    if name == player_2_last_data.post.state:
                        try:
                            if (i - combo_data[1][-1].attacks[-1].end_frame) <= 2:
                                combo_data[1][-1].attacks[-1].end_frame += 1
                        except IndexError:
                            pass  # Late hit move, disregard
                        pass  # only add a move on the first frame it appears
                    attack = Attack(name, i)
                    try:  # ensure there is a combo to add the move to
                        last_combo = combo_data[1][-1]
                        if last_combo.finished:
                            combo = Combo(i)
                            combo_data[1].append(combo)
                    except IndexError:
                        combo = Combo(i)
                        combo_data[1].append(combo)
                    combo_data[1][-1].attacks.append(attack)
                else:
                    pass  # The attack didn't hit

            # UPDATE PLAYER 2 COMBOS
            if player_1_state == STATE_CLASSIFIER_NEUTRAL or player_1_state == STATE_CLASSIFIER_MOVING_GROUND:
                # player 1 has escaped the combo, start the frame tally
                player_1_free = True
            elif player_1_state == STATE_CLASSIFIER_DOWNED_GROUND or player_1_state == STATE_CLASSIFIER_DOWNED_AIR:
                # player 1 has gotten hit again, resume combo
                player_1_free = False
                try:
                    last_combo = combo_data[1][-1]
                    if not last_combo.finished:
                        last_combo.combo_end_tally = 0
                except IndexError:
                    pass
            elif player_1_state == STATE_CLASSIFIER_DEAD:
                # End the last combo due to leading to a kill
                player_1_free = True
                try:
                    last_combo = combo_data[1][-1]
                    if not last_combo.finished:
                        last_combo = combo_data[1][-1]
                        last_combo.finished = True
                        last_combo.kill = True
                        last_combo.end_frame = i
                except IndexError:
                    pass
            else:
                if player_1_free:
                    try:
                        last_combo = combo_data[1][-1]
                        if not last_combo.finished:
                            last_combo.combo_end_tally += 1
                            if last_combo.combo_end_tally >= COMBO_FRAME_THRESHOLD:
                                last_combo.finished = True
                                last_combo.end_frame = i
                    except IndexError:
                        pass

        player_1_last_data = player_1_data
        player_2_last_data = player_2_data

    calculatePercentages(game_stats['game'], combo_data)
    return combo_data

def calculatePercentages(game, combo_data):
    # calculate percentages and trim data from getComboData
    for i, player_combo in enumerate(combo_data):
        for combo in player_combo:
            combo.percent_start = game.frames[combo.start_frame].ports[(i+1)%2].leader.post.damage
            combo.percent_end = combo.percent_start
            for attack in combo.attacks:
                start_percent = game.frames[attack.start_frame].ports[(i+1)%2].leader.post.damage
                end_percent = game.frames[attack.end_frame].ports[(i+1)%2].leader.post.damage
                attack.percent = end_percent - start_percent
            combo.attacks = [attack for attack in combo.attacks if attack.percent >= ATTACKS_PERCENT_THRESHOLD]
            for attack in combo.attacks:
                combo.percent_end += attack.percent
            combo.percent_total = combo.percent_end - combo.percent_start
        combo_data[i] = [combo for combo in combo_data[i] if combo.percent_total > COMBO_PERCENT_THRESHOLD]
        combo_data[i] = [combo for combo in combo_data[i] if len(combo.attacks) >= COMBO_ATTACKS_THRESHOLD]

def getComboStats(game_stats):
    # Calculate stats about combos
    combo_stats = [{}, {}] # player1, player2
    for i, player_combo in enumerate(game_stats['combo_data']):
        combo_stats[i]['num_combos'] = len(player_combo)
        combo_stats[i]['avg_percent'] = getComboAveragePercent(player_combo)
        combo_stats[i]['combos_per_stock'] = getCombosPerStock(player_combo, game_stats, i)
    return combo_stats

def getComboAveragePercent(combos):
    total_percent = 0
    for combo in combos:
        total_percent += combo.percent_total
    return total_percent/len(combos)

def getCombosPerStock(combos, game_stats, player):
    opponent_stocks = game_stats['game'].frames[-1].ports[(player+1)%2].leader.post.stocks
    num_stocks = 4 # hardcode this to 4 stock games because we ain't savages
    return len(combos)/(num_stocks-opponent_stocks)

def printComboData(game_stats):
    output = ""
    for i, player_combos in enumerate(game_stats['combo_data']):
        output += "Player {} Combos  :\n".format(i+1)
        output += "Total Combos     : {}\n".format(game_stats['combo_stats'][i]['num_combos'])
        output += "Combos Per Stock : {}\n".format(game_stats['combo_stats'][i]['combos_per_stock'])
        output += "Avg. Combo %     : {}\n".format(game_stats['combo_stats'][i]['avg_percent'])
        for combo in game_stats['combo_data'][i]:
            output += str(combo) + "\n"
    return output
