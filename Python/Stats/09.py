import numpy as np 
import matplotlib.pyplot as plt 

# Generating sample data 
np.random.seed(0) 
x = np.random.rand(100) 
y = 2 * x + np.random.normal(0, 0.1, 100) # Linear relationship with noise 

# --- Correlation and Regression Functions (No changes needed) ---
def pearson_correlation(x, y): 
    n = len(x) 
    sum_x = np.sum(x) 
    sum_y = np.sum(y) 
    sum_x2 = np.sum(x**2) 
    sum_y2 = np.sum(y**2) 
    sum_xy = np.sum(x * y) 
    numerator = n * sum_xy - sum_x * sum_y 
    denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) 
    return numerator / denominator 

def spearman_rank_correlation(x, y): 
    rank_x = np.argsort(np.argsort(x)) 
    rank_y = np.argsort(np.argsort(y)) 
    return pearson_correlation(rank_x, rank_y) 

def linear_regression(x, y): 
    n = len(x) 
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - 
(np.sum(x)**2)) 
    b = (np.sum(y) - m * np.sum(x)) / n 
    return m, b 

# --- Calculations ---
correlation = pearson_correlation(x, y) 
print(f"Pearson Correlation Coefficient: {correlation}") 

rank_correlation = spearman_rank_correlation(x, y) 
print(f"Spearman Rank Correlation Coefficient: {rank_correlation}") 

slope, intercept = linear_regression(x, y) 
print(f"Linear Regression: Slope = {slope}, Intercept = {intercept}") 

# --- FIXED PLOTTING ---
# Create a figure with 1 row and 2 columns for our plots
# 'ax1' is the first plot, 'ax2' is the second
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Scatter Plot (on ax1)
ax1.scatter(x, y, label='Data Points') 
ax1.plot(x, slope * x + intercept, color='red', label='Regression Line') 
ax1.set_xlabel('X') 
ax1.set_ylabel('Y') 
ax1.set_title('Scatter Plot with Regression Line') 
ax1.legend() 

# Plot 2: Correlation Matrix (on ax2)
correlation_matrix = np.corrcoef(x, y) 
# Note: we use ax2.imshow, not plt.imshow
im = ax2.imshow(correlation_matrix, cmap='hot', interpolation='nearest') 
# We need to tell the colorbar which axis to attach to
fig.colorbar(im, ax=ax2) 
ax2.set_title('Correlation Matrix Heat Map') 
ax2.set_xticks([0, 1], ['X', 'Y']) 
ax2.set_yticks([0, 1], ['X', 'Y']) 

# Adjust layout to prevent plots from overlapping
plt.tight_layout()

# Show the single figure with both plots
plt.show()

# We don't need the separate function call anymore
# plot_correlation_matrix(x, y)