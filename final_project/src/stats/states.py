from src.data_processing.classifier import STATE_NAMES


def getStateRatios(state_data):
    """

    :param state_data:
    :return: state_ratios
    [{state: (tally, ratio)}, {state: (tally, ratio)}]
    """
    state_ratios = []
    for i in range(len(state_data[0])):
        state_tally = [0]*len(STATE_NAMES)
        for frame in state_data:
            state_tally[frame[i]-1] += 1
        player_ratios = {}
        for key, value in STATE_NAMES.items():
            player_ratios[value] = (state_tally[key-1], round(100*state_tally[key-1]/len(state_data)))
        state_ratios.append(player_ratios)
    return state_ratios

def printStateRatios(state_ratios):
    string = "---State Ratios---\n"
    for i, player in enumerate(state_ratios):
        string += "Player {}:\n".format(i)
        for state, data in player.items():
            string += " {}: {}%\n".format(state, data[1])

    return string
