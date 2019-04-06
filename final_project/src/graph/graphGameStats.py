import matplotlib.pyplot as plt

from src.data_processing.classifier import STATE_CLASSIFIER_MISC
from src.graph.constants import GRAPHS_FILE_TEMPLATE


def graphGameStats(game_stats, filename_template):
    try:
        graphStateData(game_stats['state_ratios'], filename_template)
    except KeyError:
        pass

def graphStateData(state_ratios, filename_template):
    for i, player in enumerate(state_ratios):
        array = []
        labels = []
        for state, data in player.items():
            if state is not STATE_CLASSIFIER_MISC:
                labels.append(state)
                array.append(data[0])
        plt.pie(array, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        filename = filename_template.format("-player{}-state_data".format(str(i)))
        plt.savefig(GRAPHS_FILE_TEMPLATE.format(filename), bbox_inches='tight')
        plt.close()
