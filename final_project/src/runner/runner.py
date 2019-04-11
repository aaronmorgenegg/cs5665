import os

from src.data_processing.combos import printComboData
from src.data_processing.parser import parseFile
from src.graph.fileIO import writeToFile, createDirectory
from src.graph.graphGameStats import graphGameStats
from src.stats.stats import getGameStats


def runTrial(directory, filename):
    """Run these functions on the given filename"""
    game = parseFile(directory + filename)
    game_stats = getGameStats(game)
    path = "{}/output/{}/".format(os.getcwd(), filename.split(".slp")[0])
    createDirectory(path)
    graphGameStats(game_stats, "{}{}".format(path, "{}"))
    writeToFile(printComboData(game_stats), "{}{}".format(path, "combo_data.txt"))
    return game_stats

def runMultipleTrials(directory):
    """Run trial on every slp file in directory"""
    for filename in os.listdir(directory):
        if filename.endswith(".slp"):
            runTrial(directory, filename)

    # TODO: run aggregate trials, looking at data across multiple games
