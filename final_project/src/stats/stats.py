from src.data_processing.classifier import getStateData
from src.stats.settings import STATE_RATIOS, STATE_DATA
from src.stats.states import getStateRatios


def getGameStats(game):
    """

    :param game: Slippi game object
    :return: Stats
    """
    game_stats = {'game': game}
    if STATE_DATA:
        game_stats['state_data'] = getStateData(game)

        if STATE_RATIOS: game_stats['state_ratios'] = getStateRatios(game_stats['state_data'])

    return game_stats
