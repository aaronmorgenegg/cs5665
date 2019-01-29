# -*- coding: utf-8 -*-
"""
Quick introduction to the 93cars data.

Here we try to predict MidrangePrice from HighwayMPG.

-Doug Galarus, CS 5665, Spring 2019
"""

import pandas
import numpy
import matplotlib.pyplot
import sklearn.linear_model
import matplotlib.pyplot as plt


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


# Read in the data using Pandas. The result is stored in a Pandas Data Frame.
df = pandas.read_csv("93cars.csv")
pr = pandas.DataFrame({'cols': range(100)})
hh = list("0000000110001101000000111011010010110111110110110111111000110011110110000011111000001001010110110010")
hh = [int(x) for x in hh]
ph = pandas.DataFrame({'cols': hh})

# Assign to X and y. We have to reshape X to match
# what the subsequent method expects.
X = pr['cols'].values.reshape(-1, 1)
y = ph['cols'].values

# Specify the model.
model = sklearn.linear_model.LinearRegression(fit_intercept=True)

# Fit the data to the model.
model.fit(X,y)

# Extract the coeffecients. 
print("omega0 (intercept) =",model.intercept_)
print("omega1 (slope) =", model.coef_[0])

# Compute SSE and R-squared. 
predicted = model.predict(X)
SSE = ((predicted - y)**2).sum()
print("SSE = ", SSE)
R_sq = model.score(X,y)
print("R-squared = ", R_sq)

# The predict function can be applied to a vector. Here we apply to it a 
# sequence of evenly-spaced values corresponding to our x-axis.
xfit = numpy.linspace(0,100,10).reshape(-1,1)
yfit = model.predict(xfit)

# Plot the data
matplotlib.pyplot.scatter(X,y)
matplotlib.pyplot.title('Hot Hands Data')
matplotlib.pyplot.xlabel('Shot #')
matplotlib.pyplot.ylabel('Result')
matplotlib.pyplot.plot(xfit,yfit)


# Permutation Test


p_diff_Jazz = 0.001584158415841584 # The slope of hot hands linear fit
NUMITERATIONS = 100000
p_diffs = []
winloss_arr_shuffled = numpy.copy(hh)
for i in range(NUMITERATIONS):
    numpy.random.shuffle(winloss_arr_shuffled)
    p_win_after_win, p_win_after_loss, p_diff = ComputeStreakPDiff(winloss_arr_shuffled)    
    p_diffs.append(p_diff)
    
bins = numpy.round(numpy.arange(-1.0,1.01,.01),2)

numpy.histogram(p_diffs,bins)

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
