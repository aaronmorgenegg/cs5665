from src.data_processing.classifier import STATE_NAMES


def getStateRatios(state_data):
    """

    :param state_data:
    :return: state_ratios
    [{state: ([ally, ratio]}, {state: [tally, ratio]}]
    """
    state_ratios = []
    for i in range(len(state_data[0])):
        state_tally = [0]*len(STATE_NAMES)
        for frame in state_data:
            state_tally[frame[i]-1] += 1
        player_ratios = {}
        for key, value in STATE_NAMES.items():
            player_ratios[value] = [state_tally[key-1], round(100*state_tally[key-1]/len(state_data))]
        state_ratios.append(player_ratios)
    return state_ratios

def getStateRatioAirGround(state_ratios):
    """

    :param state_ratios:
    :return: [{air: [tally, ratio]}, {ground: [tally, ratio]}, {other: [tally, ratio]}]
    """
    ratios = []
    air_states = ['moving_air', 'attack_air', 'downed_air']
    ground_states = ['moving_ground', 'attack_ground', 'downed_ground', 'neutral']
    for i in range(len(state_ratios)):
        ratios.append({'air': [0, 0], 'ground': [0, 0], 'other': [0, 0]})
        for state in state_ratios:
            for name, data in state.items():
                if name in air_states:
                    ratios[i]['air'][0] += data[0]
                    ratios[i]['air'][1] += data[1]
                elif name in ground_states:
                    ratios[i]['ground'][0] += data[0]
                    ratios[i]['ground'][1] += data[1]
                else:
                    ratios[i]['other'][0] += data[0]
                    ratios[i]['other'][1] += data[1]
    return ratios


def getStateRatioAttackDefend(state_ratios):
    """

    :param state_ratios:
    :return: [{attack: [tally, ratio]}, {defense: [tally, ratio]}, {other: [tally, ratio]}]
    """
    ratios = []
    attack_states = ['attack_ground', 'attack_air']
    defense_states = ['downed_ground', 'downed_air', 'dead', 'shield', 'dodge']
    for i in range(len(state_ratios)):
        ratios.append({'attack': [0, 0], 'defense': [0, 0], 'other': [0, 0]})
        for state in state_ratios:
            for name, data in state.items():
                if name in attack_states:
                    ratios[i]['attack'][0] += data[0]
                    ratios[i]['attack'][1] += data[1]
                elif name in defense_states:
                    ratios[i]['defense'][0] += data[0]
                    ratios[i]['defense'][1] += data[1]
                else:
                    ratios[i]['other'][0] += data[0]
                    ratios[i]['other'][1] += data[1]
    return ratios

def printStateRatios(state_ratios):
    string = "---State Ratios---\n"
    for i, player in enumerate(state_ratios):
        string += "Player {}:\n".format(i)
        for state, data in player.items():
            string += " {}: {}%\n".format(state, data[1])

    return string
