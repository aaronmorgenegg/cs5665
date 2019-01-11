# -*- coding: utf-8 -*-
"""
Created originally on Mon Apr 23 11:22:49 2018

@author: Doug

Determines if the 2017-2018 Jazz were a "streakish" team.
"""
import numpy as np
import matplotlib.pyplot as plt

# String of wins(1) and losses (0) for the 2017-2018 Utah Jazz:
winloss_str = "0000000110001101000000111011010010110111110110110111111000110011110110000011111000001001010110110010"
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
# Simulate a bunch of seasons and track the statistic.
# Show a histogram of the results.
NUMITERATIONS = 100000
p_diffs = []
winloss_arr_shuffled = np.copy(winloss_arr)
for i in range(NUMITERATIONS):
    np.random.shuffle(winloss_arr_shuffled)
    p_win_after_win, p_win_after_loss, p_diff = ComputeStreakPDiff(winloss_arr_shuffled)    
    p_diffs.append(p_diff)
    
bins = np.round(np.arange(-1.0,1.01,.01),2)

np.histogram(p_diffs,bins)

plt.hist(p_diffs,bins)
plt.title("Histogram of\np_win_after_win - p_win_after_loss Statistic\nfor the 2017-2018 Jazz Season")
plt.xlabel("p_win_after_win - p_win_after_loss")
plt.ylabel("Count")
plt.xlim(-.5,.5)
plt.show()
###############################################################################



###############################################################################
# Compute the p-value.
# Is it significant?
p_diffs.sort()
idx = np.searchsorted(p_diffs, p_diff_Jazz)
p_value_Jazz = 1.0 - (idx + 1) / NUMITERATIONS

print("The test statistic for the 2017-2018 Jazz is: ", p_diff_Jazz)
print("The p-value for the p_win_after_win - p_win_after_loss statistic for the 2017-2018 Jazz is: ", p_value_Jazz)
print("For alpha=0.05, the cutoff would be: ",p_diffs[int(0.95*NUMITERATIONS)])
###############################################################################

###############################################################################
