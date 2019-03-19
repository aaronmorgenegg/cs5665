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
