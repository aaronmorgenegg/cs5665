import os

from src.data_processing.parser import parseFile
from src.graph.graphGameStats import graphGameStats
from src.stats.stats import getGameStats


def runTrial(directory, filename):
    """Run these functions on the given filename"""
    game = parseFile(directory + filename)
    game_stats = getGameStats(game)
    graphGameStats(game_stats, "{}{}".format(filename, "{}"))

def runMultipleTrials(directory):
    """Run trial on every slp file in directory"""
    for filename in os.listdir(directory):
        if filename.endswith(".slp"):
            runTrial(directory, filename)
