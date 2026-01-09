import numpy as np
from scipy import stats

data = [(1, 5), (2, 10), (3, 15), (4, 20), (5, 10)]
expanded_data = []
for value, frequency in data:
    expanded_data.extend([value] * frequency)
expanded_data = np.array(expanded_data)
mean = np.mean(expanded_data)
median=np.median(expanded_data)
mode =stats.mode(expanded_data)[0][0]
variance = np.var(expanded_data)
std_deviation = np.std(expanded_data)
mean_deviation = np.mean(np.abs(expanded_data- mean))
Q1 =np.percentile(expanded_data, 25)
Q3 =np.percentile(expanded_data, 75)
quartile_deviation = (Q3- Q1) / 2
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Mean Deviation: {mean_deviation}")
print(f"Quartile Deviation: {quartile_deviation}")