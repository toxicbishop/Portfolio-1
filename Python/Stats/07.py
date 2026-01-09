import math
def one_sample_t_test(sample, population_mean):
    sample_mean = sum(sample) / len(sample)
    sample_std = math.sqrt(sum((x - sample_mean) ** 2 for x in sample) / (len(sample) - 1))
    t_statistic = (sample_mean - population_mean) / (sample_std / math.sqrt(len(sample)))
    return t_statistic, sample_mean
sample_data = [2.3, 2.5, 2.8, 3.0, 2.7]
population_mean = 2.5
t_statistic, sample_mean = one_sample_t_test(sample_data, population_mean)
print(f"One-Sample T-Test: t-statistic = {t_statistic}, Sample Mean = {sample_mean}")
def two_sample_t_test(sample1, sample2):
    mean1 = sum(sample1) / len(sample1)
    mean2 = sum(sample2) / len(sample2)
    std1 = math.sqrt(sum((x - mean1) ** 2 for x in sample1) / (len(sample1) - 1))
    std2 = math.sqrt(sum((x - mean2) ** 2 for x in sample2) / (len(sample2) - 1))
    pooled_std = math.sqrt(((len(sample1) - 1) * std1**2 + (len(sample2) - 1) * std2**2) /
    (len(sample1) + len(sample2) - 2))
    t_statistic = (mean1 - mean2) / (pooled_std * math.sqrt(1/len(sample1) + 1/len(sample2)))
    return t_statistic, mean1, mean2
sample_data1 = [2.3, 2.5, 2.8, 3.0, 2.7]
sample_data2 = [3.1, 3.3, 3.5, 3.7, 3.6]
t_statistic, mean1, mean2 = two_sample_t_test(sample_data1, sample_data2)
print(f"Two-Sample T-Test: t-statistic = {t_statistic}, Sample Mean 1 = {mean1}, Sample Mean 2 ={mean2}")
def paired_sample_t_test(sample1, sample2):
    differences = [x - y for x, y in zip(sample1, sample2)]
    mean_diff = sum(differences) / len(differences)
    std_diff = math.sqrt(sum((d - mean_diff) ** 2 for d in differences) / (len(differences) - 1))
    t_statistic = mean_diff / (std_diff / math.sqrt(len(differences)))
    return t_statistic, mean_diff
sample_data1 = [2.3, 2.5, 2.8, 3.0, 2.7]
sample_data2 = [2.1, 2.4, 2.6, 2.9, 2.5]