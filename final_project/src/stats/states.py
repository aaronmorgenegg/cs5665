from src.data_processing.classifier import STATE_NAMES


def getStateRatios(game, state_data):
    state_ratios = []
    for i in range(len(state_data[0])):
        state_tally = [0]*len(STATE_NAMES)
        for frame in state_data:
            state_tally[frame[i]-1] += 1
        player_ratios = {}
        for key, value in STATE_NAMES.items():
            player_ratios[value] = 100*state_tally[key-1]/len(state_data)
        state_ratios.append(player_ratios)
    return state_ratios

def printStateRatios(state_ratios):
    string = ""
    for i, player in enumerate(state_ratios):
        string += "Player {}:\n".format(i)
        for state, ratio in player.items():
            string += " {}: {}%\n".format(state, round(ratio))

    return string
