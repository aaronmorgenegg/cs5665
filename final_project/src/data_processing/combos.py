from src.data_processing.classifier import STATE_CLASSIFIER_ATTACK_GROUND, STATE_CLASSIFIER_ATTACK_AIR, \
    STATE_CLASSIFIER_DOWNED_GROUND, STATE_CLASSIFIER_DOWNED_AIR, STATE_CLASSIFIER_SHIELD, STATE_CLASSIFIER_NEUTRAL, \
    STATE_CLASSIFIER_MOVING_GROUND, STATE_CLASSIFIER_DEAD

COMBO_FRAME_THRESHOLD = 60 # Number of frames the defender must be in a grounded, 'active' state before a combo 'ends'


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

class Attack:
    def __init__(self, name, start_frame):
        self.name = name
        self.start_frame = start_frame
        self.end_frame = start_frame
        self.percent = 0

def getComboData(game_stats):
    """
    Analyze framedata/state_data and mark combos

    :param game_stats: game_stats object from stats.py
    :return: combo data
    """
    combo_data = [[], []] # player 1, player 2
    player_1_last_data = None
    player_2_last_data = None
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
            # TODO: identify attacks that are part of a combo
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
                # update combo frame tally, check if player 2 has escaped combo
                try:
                    last_combo = combo_data[0][-1]
                    if not last_combo.finished:
                        last_combo.combo_end_tally += 1
                        if last_combo.combo_end_tally >= COMBO_FRAME_THRESHOLD:
                            last_combo.finished = True
                            last_combo.end_frame = i
                except IndexError:
                    pass
            elif player_2_state == STATE_CLASSIFIER_DEAD:
                # End the last combo due to leading to a kill
                try:
                    last_combo = combo_data[0][-1]
                    last_combo.finished = True
                    last_combo.kill = True
                    last_combo.end_frame = i
                except IndexError:
                    pass
            else:
                # Set the last combo frame tally to 0 as the combo continues
                try:
                    last_combo = combo_data[0][-1]
                    if not last_combo.finished:
                        last_combo.combo_end_tally = 0
                except IndexError:
                    pass

            # TODO: player 2 combos player 1
            # TODO: need to look at start and end frames for all attacks and combos and calculate percent diff

        player_1_last_data = player_1_data
        player_2_last_data = player_2_data

    return combo_data
