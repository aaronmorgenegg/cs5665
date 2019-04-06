from src.data_processing.classifier import getStateData
from src.stats.settings import STATE_RATIOS, STATE_DATA
from src.stats.states import getStateRatios, getStateRatioAirGround, getStateRatioAttackDefend


def getGameStats(game):
    """

    :param game: Slippi game object
    :return: Stats
    """
    game_stats = {'game': game}
    if STATE_DATA:
        game_stats['state_data'] = getStateData(game)

        if STATE_RATIOS:
            game_stats['state_ratios'] = getStateRatios(game_stats['state_data'])
            game_stats['state_ratio_air_ground'] = getStateRatioAirGround(game_stats['state_ratios'])
            game_stats['state_ratio_attack_defend'] = getStateRatioAttackDefend(game_stats['state_ratios'])

    return game_stats
