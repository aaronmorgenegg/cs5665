import sys

from src.runner.runner import runMultipleTrials, runTrial

if len(sys.argv) < 2:
    runMultipleTrials("../data/personal/")
else:
    filename = sys.argv[1].split("/")[-1]
    directory = sys.argv[1].split(filename)[0]
    runTrial(directory, filename)


# for i, frame in enumerate(game.frames):
#     print("Frame: {}".format(i))
#     for j, port in enumerate(frame.ports):
#         if state_data[i][j] is not None: print(" Port {}: {} {}%".format(j, state_data[i][j], port.leader.post.damage))
#     print()
