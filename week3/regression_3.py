# Import the required libraries
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_df = pd.read_csv('./train-data-used_car.csv')

#print (data_df.head())
#print (data_df.columns)

#data_np = data_df.to_numpy()
data_df = data_df.dropna()
X_df = data_df[['Year','Kilometers_Driven','Seats']]
y_df = data_df[['Price']]


X =X_df.to_numpy()
y = y_df.to_numpy()

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_), print(lin_reg.coef_)