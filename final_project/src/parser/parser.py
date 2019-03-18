import slippi


def parseFile(filename):
    """
    Return a slippi game object from a filename

    :param filename: filename to be read
    :return: slippi game object
    :seealso: https://py-slippi.readthedocs.io/en/latest/source/slippi.html#module-slippi.game
    """
    game = slippi.Game(filename)
    return game


def tempParseFile():
    """
    Dummy function for testing how parsing works
    :return:
    """
    game = parseFile('data/pro/3-stream-Game_20190309T212217.slp') # zain vs swedish delight at gang 2
    print(game.metadata)
    print(game.start)
    print(game.end)
    for frame in game.frames:
        for port in frame.ports:
            if port is not None:
                data = port.leader  # see also: port.follower (ICs)
                string = str(data.post.character)
                string += ": "
                string += str(data.post.state)
                print(string)  # character's post-frame action state


# tempParseFile()
