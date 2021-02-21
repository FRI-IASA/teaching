# Import the required libraries
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load up the files 
# Windows users, you may need to change the train.csv
# path to '.\train.csv'
data_df = pd.read_csv('./train.csv')
data_np = data_df.to_numpy()

print (data_np.shape)
print (data_np[0,:])   # First row
print (data_np[-1,:])  # Last row

X = data_np[:,0]  # First column 
y = data_np[:,1]   # Second column
plt.plot(X,y,'.')
plt.show()

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
X = X.reshape(-1,1)
y = y.reshape(-1,1)
lin_reg.fit(X, y)
print(lin_reg.intercept_), print(lin_reg.coef_)

y_hat = lin_reg.intercept_ +lin_reg.coef_*X

plt.plot(X,y,'.')
plt.plot(X,y_hat,'-')
plt.show()