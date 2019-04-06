import os

from src.data_processing.classifier import getStateData
from src.data_processing.parser import parseFile
from src.graph.graphGameStats import graphGameStats
from src.stats.states import getStateRatios, printStateRatios

# Local file for testing/running functions
from src.stats.stats import getGameStats

for filename in os.listdir("../data/personal/"):
    if filename.endswith(".slp"):
        game = parseFile('../data/personal/{}'.format(filename))
        game_stats = getGameStats(game)
        graphGameStats(game_stats, "{}{}".format(filename, "{}"))

# for i, frame in enumerate(game.frames):
#     print("Frame: {}".format(i))
#     for j, port in enumerate(frame.ports):
#         if state_data[i][j] is not None: print(" Port {}: {} {}%".format(j, state_data[i][j], port.leader.post.damage))
#     print()
