# -*- coding: utf-8 -*-
"""
Created originally on Mon Apr 23 11:22:49 2018

@author: Doug

Determines if the 2017-2018 Jazz were a "streakish" team.
"""
import numpy as np
import matplotlib.pyplot as plt

# String of wins(1) and losses (0) for the 2017-2018 Utah Jazz:
winloss_str = "1010011100001000101111110000100010001000100101011111111111010111111111010101111110"
# Change the string into a list of integers.
winloss_arr = [int(c) for c in winloss_str]

###############################################################################
# Show a barchart of wins and losses.
# Shows wins as blue, positive bars.
# Shows losses as red, negative bars.
def PlotWinsAndLosses(wins,title):
    
    win_indexes = [i for i in range(len(wins)) if wins[i]]
    win_vals = [1 for w in wins if w]
    
    loss_indexes = [i for i in range(len(wins)) if not wins[i]]
    loss_vals = [-1 for w in wins if not w]
    
    ax = plt.gca()
    ax.bar(win_indexes, win_vals, color="blue", width=1)
    ax.bar(loss_indexes, loss_vals, color="red", width=1)
    plt.title(title)
    plt.xlabel("Game")
    plt.ylabel("Win/Loss")
    
    plt.show()
###############################################################################


###############################################################################
# Computes the probabilities and differences for two consecutive games. 
# Input is a list of 1s (wins) and 0s (losses)
# Returns P(win after win) , P(win after loss), p_diff (the difference between the two)
def ComputeStreakPDiff(wins):
    # Loss after loss count.
    num_00 = 0
    # Win after loss count.
    num_01 = 0
    # Loss after win count.
    num_10 = 0
    # Win after win count.
    num_11 = 0
    # Loop from the second game to the last 
    for i in range(1,len(wins)):
        if (wins[i-1]==0):
            if (wins[i]==0):
                num_00 = num_00 + 1
            else:
                num_01 = num_01 + 1
        else:
            if (wins[i]==0):
                num_10 = num_10 + 1
            else:
                num_11 = num_11 + 1
                      
    # Probability of win following a win
    p_win_after_win = num_11 / (num_11 + num_10)
    # Probability of win following a loss
    p_win_after_loss = num_01 / (num_01 + num_00)
    
    # The difference between the probabilities    
    p_diff = p_win_after_win - p_win_after_loss
        
    return p_win_after_win, p_win_after_loss, p_diff
###############################################################################

p_win_after_win_Jazz, p_win_after_loss_Jazz, p_diff_Jazz = ComputeStreakPDiff(winloss_arr)
PlotWinsAndLosses(winloss_arr,"Utah Jazz Wins (48) and Losses (34) 2017-2018")
print("Probability of a win after a win = ", p_win_after_win_Jazz)
print("Probability of a win after a loss = ", p_win_after_loss_Jazz)
print("p_win_after_win - p_win_after_loss = ", p_diff_Jazz)


###############################################################################
# The Jazz had 48 wins and 34 losses.
# The most streakish season they could have would be to have all the wins in
# a row and all the losses in a row.
# Look at an extreme case.
winloss_arr_example_1 = np.append(48 * [1], 34 * [0])
#winloss_arr_example_1 = np.append(34 * [0], 48 * [1])

p_win_after_win_example_1, p_win_after_loss_example_1, p_diff_example_1 = ComputeStreakPDiff(winloss_arr_example_1)
PlotWinsAndLosses(winloss_arr_example_1,"The Most Streakish 48-34 Possible Season")
print("Probability of a win after a win = ", p_win_after_win_example_1)
print("Probability of a win after a loss = ", p_win_after_loss_example_1)
print("p_win_after_win - p_win_after_loss = ", p_diff_example_1)
###############################################################################

###############################################################################
# Look at wanother extreme case. A less streakish season - anti-streakish.
# Alternate wins and losses.
winloss_arr_example_2 = np.append(34 * [1, 0], 14 * [1])

p_win_after_win_example_2, p_win_after_loss_example_2, p_diff_example_2 = ComputeStreakPDiff(winloss_arr_example_2)
PlotWinsAndLosses(winloss_arr_example_2,"An Anti-Streakish 48-34 Possible Season")
print("Probability of a win after a win = ", p_win_after_win_example_2)
print("Probability of a win after a loss = ", p_win_after_loss_example_2)
print("p_win_after_win - p_win_after_loss = ", p_diff_example_2)
###############################################################################


