import numpy as np
import matplotlib.pyplot as plt


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
plt.plot(X,y,'.')
plt.show()

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_), print(lin_reg.coef_)

y_hat = lin_reg.intercept_ +lin_reg.coef_*X

plt.plot(X,y,'.')
plt.plot(X,y_hat,'-')
plt.show()