from src.data_processing.classifier import STATE_CLASSIFIER_ATTACK_GROUND, STATE_CLASSIFIER_ATTACK_AIR

COMBO_FRAME_THRESHOLD = 60 # Number of frames the defender must be in a grounded, 'active' state before a combo 'ends'


class Combo:
    def __init__(self):
        self.start_frame = 0
        self.end_frame = 0
        self.moves = []
        self.percent_start = 0
        self.percent_end = 0
        self.percent_total = 0
        self.kill = False

def getComboData(game, state_data):
    """
    Analyze framedata/state_data and mark combos

    :param game: slippi game
    :param state_data: state data from classifier.py
    :return: combo data
    """
    combo_data = []
    for i, frame in enumerate(game.frames):
        for j, port in enumerate(frame.ports):
            if port is not None:
                data = port.leader
                # state = data.post.state
                state = state_data[i][j]
                # TODO: identify attacks that are part of a combo
                if state == STATE_CLASSIFIER_ATTACK_GROUND or STATE_CLASSIFIER_ATTACK_AIR:
                    pass

                # TODO: either start a new combo, or add the move to an existing combo

                # TODO: update last combo - keep a counter of # frames in neutral or movement states.
                # TODO: if counter exceeds the threshold set the end frame of the combo
