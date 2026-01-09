import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_breast_cancer 
data = load_breast_cancer() 
X = data.data 
y = data.target 
df = pd.DataFrame(X, columns=data.feature_names) 
print(df) 
X_mean = np.mean(X, axis=0) 
X_std = np.std(X, axis=0) 
X_standardized = (X - X_mean) / X_std 
cov_matrix = np.cov(X_standardized, rowvar=False) 
print(cov_matrix) 
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix) 
sorted_indices = np.argsort(eigenvalues)[::-1] 
eigenvalues_sorted = eigenvalues[sorted_indices] 
eigenvectors_sorted = eigenvectors[:, sorted_indices] 
k = 2 
eigenvectors_subset = eigenvectors_sorted[:, :k] 
X_pca = X_standardized.dot(eigenvectors_subset) 
plt.figure(figsize=(10, 6)) 
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50) 
plt.title('PCA of Wisconsin Breast Cancer Dataset') 
plt.xlabel('Principal Component 1') 
plt.ylabel('Principal Component 2') 
plt.colorbar(label='Class Label') 
plt.grid(True) 
plt.show()