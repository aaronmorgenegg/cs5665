import matplotlib.pyplot as plt

from src.data_processing.classifier import STATE_CLASSIFIER_MISC
from src.graph.constants import GRAPHS_FILE_TEMPLATE


def graphGameStats(game_stats, filename_template):
    graphStateData(game_stats, filename_template)

def graphStateData(game_stats, filename_template):
    try:
        state_ratios = game_stats['state_ratios']
    except KeyError:
        return
    graphOverallStateData(state_ratios, filename_template)
    graphAirGroundRatios(game_stats['state_ratio_air_ground'], filename_template)
    graphAttackDefenseRatios(game_stats['state_ratio_attack_defend'], filename_template)

def graphRatios(state_ratios, filename_template, filename_desc):
    for i, player in enumerate(state_ratios):
        array = []
        labels = []
        for state, data in player.items():
            if state is not STATE_CLASSIFIER_MISC:
                labels.append(state)
                array.append(data[0])
        graphPieChart(array, labels, filename_template, filename_desc.format(str(i)))

def graphOverallStateData(state_ratios, filename_template):
    graphRatios(state_ratios, filename_template, "player{}-state_ratio_overall")

def graphAirGroundRatios(state_ratios, filename_template):
    graphRatios(state_ratios, filename_template, "player{}-state_ratio_air_ground")

def graphAttackDefenseRatios(state_ratios, filename_template):
    graphRatios(state_ratios, filename_template, "player{}-state_ratio_attack_defense")

def graphPieChart(array, labels, filename_template, file_desc):
    plt.pie(array, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    filename = filename_template.format(file_desc)
    plt.savefig(GRAPHS_FILE_TEMPLATE.format(filename), bbox_inches='tight')
    plt.close()
