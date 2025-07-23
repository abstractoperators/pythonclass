import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([5, 20, 14, 32, 22, 38])
model = LinearRegression()

model.fit(x, y)
predictions = model.predict(x)

r_squared = model.score(x, y)

print(f"Coefficients: {r_squared}")

y_pred = model.predict(x)
print(f"Predictions: {y_pred}")