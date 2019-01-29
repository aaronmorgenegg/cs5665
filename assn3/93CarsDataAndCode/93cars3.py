# -*- coding: utf-8 -*-
"""
Quick introduction to the 93cars data.

Here we try to predict MidrangePrice from 'Length','Wheelbase','Width','HighwayMPG'.

-Doug Galarus, CS 5665, Spring 2019
"""

import pandas
import numpy
import matplotlib.pyplot
import sklearn.linear_model

# Read in the data using Pandas. The result is stored in a Pandas Data Frame.
df = pandas.read_csv("93cars.csv")

# Assign to X and y. We have to reshape X to match
# what the subsequent method expects.
X = df[['Length','Wheelbase','Width','HighwayMPG']].values.reshape(-1,4)
y = df['MidrangePrice'].values

# Specify the model.
model = sklearn.linear_model.LinearRegression(fit_intercept=True)

# Fit the data to the model.
model.fit(X,y)

# Extract the coeffecients. 
print("omega0 (intercept) =",model.intercept_)
print("omega1 =", model.coef_[0])
print("omega2 =", model.coef_[1])
print("omega3 =", model.coef_[2])
print("omega4 =", model.coef_[3])

# Compute SSE and R-squared. 
predicted = model.predict(X)
SSE = ((predicted - y)**2).sum()
print("SSE = ", SSE)

R_sq = model.score(X,y)
print("R-squared = ", R_sq)
