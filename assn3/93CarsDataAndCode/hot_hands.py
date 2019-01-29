#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:29:15 2019

@author: aaron
"""
import random

import pandas
import numpy
import matplotlib.pyplot
import sklearn.linear_model
import matplotlib.pyplot as plt


def runLinearModel(data, output=False):
    pr = pandas.DataFrame({'cols': range(100)})
    hh = list(data)
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
    if output: print("omega0 (intercept) =",model.intercept_)
    if output: print("omega1 (slope) =", model.coef_[0])

    # Compute SSE and R-squared. 
    predicted = model.predict(X)
    SSE = ((predicted - y)**2).sum()
    if output: print("SSE = ", SSE)
    R_sq = model.score(X,y)
    if output: print("R-squared = ", R_sq)

    # The predict function can be applied to a vector. Here we apply to it a 
    # sequence of evenly-spaced values corresponding to our x-axis.
    xfit = numpy.linspace(0,100,10).reshape(-1,1)
    yfit = model.predict(xfit)
    
    # Plot the data
    if output:
        matplotlib.pyplot.scatter(X,y)
        matplotlib.pyplot.title('Hot Hands Data')
        matplotlib.pyplot.xlabel('Shot #')
        matplotlib.pyplot.ylabel('Result')
        matplotlib.pyplot.plot(xfit,yfit)
        
    return model.coef_[0]


# Permutation Test

hh_data = list("0000000110001101000000111011010010110111110110110111111000110011110110000011111000001001010110110010")
hh_data = [int(x) for x in hh_data]
p_diff_Jazz = 0.001584158415841584 # The slope of hot hands linear fit
NUMITERATIONS = 100000
p_diffs = []
winloss_arr_shuffled = list(hh_data)
for i in range(NUMITERATIONS):
    if i % 100 == 0: print("Iteration: {}".format(i))
    random.shuffle(winloss_arr_shuffled)
    p_diffs.append(runLinearModel(winloss_arr_shuffled))
    
bins = numpy.round(numpy.arange(-1.0,1.01,.01),2)

numpy.histogram(p_diffs,bins)

plt.hist(p_diffs)
plt.title("Histogram of omega(slopes)\nfor linear fit of hot hands permutation data")
plt.xlabel("slope")
plt.ylabel("Count")
plt.xlim(-.02,.02)
plt.show()
###############################################################################



###############################################################################
# Compute the p-value.
# Is it significant?
p_diffs.sort()
idx = numpy.searchsorted(p_diffs, p_diff_Jazz)
p_value_Jazz = 1.0 - (idx + 1) / NUMITERATIONS

print("The test statistic for the 2017-2018 Jazz is: ", p_diff_Jazz)
print("The p-value for the p_win_after_win - p_win_after_loss statistic for the 2017-2018 Jazz is: ", p_value_Jazz)
print("For alpha=0.05, the cutoff would be: ",p_diffs[int(0.95*NUMITERATIONS)])
