from src.data_processing.classifier import STATE_CLASSIFIER_SHIELD


ESCAPE_STATE_FRAME_COUNT = 15 # number of frames to record for when a player drops shield


def getComboEscapeOutOfShieldData(game_stats):
    """

    :param game_stats:
    :return: [[], []] # player 1, player 2
    """
    shield_escape_data = [[], []]
    for i, player_combo in enumerate(game_stats['combo_data']):
        for combo in player_combo:
            combo_start = combo.start_frame
            combo_end = combo.end_frame
            for j in range(combo_start, combo_end):
                frame_state = game_stats['state_data'][j]
                other_player_data = frame_state[(i+1)%2]
                next_other_player_data = frame_state[(i+1)%2]
                if other_player_data == STATE_CLASSIFIER_SHIELD:
                    if next_other_player_data == STATE_CLASSIFIER_SHIELD:
                        pass
                    else:
                        escape_state = getEscapeState(game_stats, i, j)
                        shield_escape_data[(i+1)%2].append(escape_state)

    return shield_escape_data


def getEscapeState(game_stats, player, frame):
    escape_state = []
    for k in range(1, ESCAPE_STATE_FRAME_COUNT):
        escape_state.append(game_stats['state_data'][frame + k][(player + 1) % 2])
    # TODO have a list of states directly after shielding - should classify these somehow
    return escape_state
