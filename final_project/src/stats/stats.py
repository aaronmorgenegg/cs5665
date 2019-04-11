from src.data_processing.classifier import getStateData
from src.data_processing.combos import getComboData, getComboStats
from src.data_processing.shield import getEscapeOutOfShieldData
from src.stats.settings import STATE_RATIOS, STATE_DATA, COMBO_DATA, ESCAPE_OUT_OF_SHIELD_DATA
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
        if COMBO_DATA:
            game_stats['combo_data'] = getComboData(game_stats)
            game_stats['combo_stats'] = getComboStats(game_stats)
            game_stats['combo_stats'] = getComboStats(game_stats)
        if ESCAPE_OUT_OF_SHIELD_DATA:
            game_stats['escape_oos'] = getEscapeOutOfShieldData(game_stats)

    return game_stats
