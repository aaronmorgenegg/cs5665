from slippi.id import ActionState


STATE_CLASSIFIERS = {
    'neutral': [],
    'downed': 2, # knocked down, freefalling, hitstun
    'dead': 3, # Dead or respawn
    'wavedash': 4,
    'moving_ground': 5, # dashing, walking
    'moving_air': 6, # Jumping, falling
    'attack_ground': 7, # ground attack
    'attack_air': 8, # aerial attack
    'shield': 9, # shielding
    'dodge': 10, # rolling, spot dodge, non-wavedash airdodge'
}

def getStateData(game):
    """

    :param game: slippi game
    :return: list of frames containing discrete states
    """
    state_data = []

    for frame in game.frames:
        frame_state = []
        for port in frame.ports:
            if port is None:
                frame_state.append(None)
            else:
                data = port.leader
                state = classify(data.post.state)
                # TODO: need to check for wavedashes
                frame_state.append(state)
        state_data.append(frame_state)

    return state_data

def classify(state):
    """

    :param state: slippi game state
    :return: classified state
    :seealso: https://py-slippi.readthedocs.io/en/latest/source/slippi.html#module-slippi.id
    """
    for key, value in STATE_CLASSIFIERS.items():
        if state in value:
            return key
    raise Exception("Error: Could not classify game state: {}".format(state))
