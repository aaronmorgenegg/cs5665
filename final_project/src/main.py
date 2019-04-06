from src.runner.runner import runMultipleTrials

runMultipleTrials("../data/personal/")

# for i, frame in enumerate(game.frames):
#     print("Frame: {}".format(i))
#     for j, port in enumerate(frame.ports):
#         if state_data[i][j] is not None: print(" Port {}: {} {}%".format(j, state_data[i][j], port.leader.post.damage))
#     print()
