import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 
iris = sns.load_dataset('iris') 
print(iris.head()) 
X = iris[['sepal_length', 'sepal_width', 'petal_width']] 
y = iris['petal_length'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
model = LinearRegression() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
mse = mean_squared_error(y_test, y_pred) 
r2 = r2_score(y_test, y_pred) 
print(f'Mean Squared Error: {mse}') 
print(f'R-squared: {r2}') 
plt.figure(figsize=(10, 6)) 
plt.scatter(y_test, y_pred, color='blue') 
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=2) 
plt.title('Actual vs Predicted Petal Length') 
plt.xlabel('Actual Petal Length') 
plt.ylabel('Predicted Petal Length') 
plt.grid() 
plt.show()