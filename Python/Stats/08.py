import numpy as np
group1 = [23,20,22,25,30]
group2 = [30,32,29,35,31]
group3 = [25,27,24,22,26]
data = [group1,group2,group3]
group_means = [np.mean(group) for group in data]
overall_mean = np.mean([item for group in data for item in group])
SSB = sum(len(group)*(mean- overall_mean)**2 for group,mean in zip(data,group_means))
SSW = sum(sum((x - mean)**2 for x in group) for group,mean in zip(data,group_means))
df_between = len(data)-1
df_within = sum(len(group) for group in data) - len(data)
MSB = SSB / df_between
MSW = SSW / df_within 
F_statistic = MSB / MSW
print(f" F-Statistics for one-way ANOVA : {F_statistic}")
factor_A = [[23,20,22],[30,32,29],[25,27,24]]
factor_B = [[25,30,28],[22,20,21],[27,29,26]]
means_A = [np.mean([factor_A[i][j] for i in range(len(factor_A))]) for j in range(len(factor_A[0]))]
means_B = [np.mean([factor_B[i][j] for i in range(len(factor_B))]) for j in range(len(factor_B[0]))]
overall_mean = np.mean([item for sublist in factor_A for item in sublist] + [item for sublist in factor_B for item in sublist])
SS_A = sum(len(factor_B[0])*(mean - overall_mean)**2 for mean in means_A)
SS_B = sum(len(factor_A[0])*(mean - overall_mean)**2 for mean in means_B)
SS_AB = sum((np.mean(factor_A[i]) - overall_mean)**2 for i in range(len(factor_A)))
SST = SS_A + SS_B + SS_AB
df_A = len(factor_A) - 1
df_B = len(factor_B) - 1
df_AB = df_A * df_B
MS_A = SS_A / df_A
MS_B = SS_B / df_B
MS_AB = SS_AB / df_AB
F_A =  MS_A /(SST /(len(factor_A)* len(factor_B) - 1))
F_B =  MS_B /(SST /(len(factor_A)* len(factor_B) - 1))
print(f"F-Statistic for Factor A : {F_A}")
print(f"F-Statistic for Factor B : {F_B}")