from src.data_processing.classifier import STATE_CLASSIFIER_ATTACK_GROUND, STATE_CLASSIFIER_ATTACK_AIR, \
    STATE_CLASSIFIER_DOWNED_GROUND, STATE_CLASSIFIER_DOWNED_AIR, STATE_CLASSIFIER_SHIELD

COMBO_FRAME_THRESHOLD = 60 # Number of frames the defender must be in a grounded, 'active' state before a combo 'ends'


class Combo:
    def __init__(self):
        self.start_frame = 0
        self.end_frame = 0
        self.attacks = []
        self.percent_start = 0
        self.percent_end = 0
        self.percent_total = 0
        self.kill = False

class Attack:
    def __init__(self, name, start_frame, percent):
        self.name = name
        self.start_frame = start_frame
        self.end_frame = start_frame
        self.percent = percent

def getComboData(game_stats):
    """
    Analyze framedata/state_data and mark combos

    :param game_stats: game_stats object from stats.py
    :return: combo data
    """
    combo_data = []
    player_1_last_data = None
    player_1_last_state = None
    player_2_last_data = None
    player_2_last_state = None
    for i, frame in enumerate(game_stats['game'].frames):
        if i == 0: pass
        else:
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
            # TODO: identify attacks that are part of a combo
            if player_1_state == STATE_CLASSIFIER_ATTACK_GROUND or STATE_CLASSIFIER_ATTACK_AIR:
                if player_2_state == STATE_CLASSIFIER_DOWNED_GROUND or STATE_CLASSIFIER_DOWNED_AIR or STATE_CLASSIFIER_SHIELD:
                    pass # The attack hit
                else:
                    pass # The attack didn't hit

            # TODO: either start a new combo, or add the move to an existing combo

            # TODO: update last combo - keep a counter of # frames in neutral or movement states.
            # TODO: if counter exceeds the threshold set the end frame of the combo

            player_1_last_data = player_1_data
            player_1_last_state = player_1_state
            player_2_last_data = player_2_data
            player_2_last_state = player_2_state
