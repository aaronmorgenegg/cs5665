# -*- coding: utf-8 -*-
"""
Quick introduction to the 93cars data.

Here we try to predict MidrangePrice from 'Length','Wheelbase','Width'.

-Doug Galarus, CS 5665, Spring 2019
"""

import pandas
import numpy
import matplotlib.pyplot
import sklearn.linear_model

# Read in the data using Pandas. The result is stored in a Pandas Data Frame.
df = pandas.read_csv("93cars.csv")
hr = pandas.DataFrame({'cols': range(100)})
hh = list("0000000110001101000000111011010010110111110110110111111000110011110110000011111000001001010110110010")
ph = pandas.DataFrame({'col': hh})

# Assign to X and y. We have to reshape X to match
# what the subsequent method expects.
X = hr['col'].values
y = hh['col'].values

# Specify the model.
model = sklearn.linear_model.LinearRegression(fit_intercept=True)

# Fit the data to the model.
model.fit(X,y)

# Extract the coeffecients. 
print("omega0 (intercept) =",model.intercept_)
print("omega1 =", model.coef_[0])
print("omega2 =", model.coef_[1])
print("omega3 =", model.coef_[2])

# Compute SSE and R-squared. 
predicted = model.predict(X)
SSE = ((predicted - y)**2).sum()
print("SSE = ", SSE)
R_sq = model.score(X,y)
print("R-squared = ", R_sq)
