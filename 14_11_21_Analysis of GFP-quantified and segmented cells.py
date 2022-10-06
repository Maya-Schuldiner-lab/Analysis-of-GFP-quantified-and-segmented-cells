import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# load raw data file
data = pd.read_csv('ParameterData_Main.csv')

# remove cells out of gate (ROI)
data = data[data['R01'] == 1].reset_index(drop=True)

# remove cells in position 1
data = data[data['Position '] != 1].reset_index(drop=True)

# sample 500 cells from each well and export data for plotting
wells = pd.unique(data['Well '])  # get list of wells
sampled_data = pd.DataFrame()
for w in wells:
    sampled_data = pd.concat([sampled_data, data[data['Well '] == w].sample(n=500)])
# replace well number
sampled_data = sampled_data.replace({194: 2, 195: 3, 196: 4, 197: 5, 198: 6, 199: 7, 200: 8, 201: 9, 202: 10, 203: 11})
# export data for plotting to csv
sampled_data.to_csv('sampled data.csv', index=False)

# plot

sns.boxplot(data=sampled_data[np.logical_or(sampled_data['Well '] == 2, sampled_data['Well '] == 7)], x='Well ', y='Mean Intensity 488nm')
plt.show()

sns.boxplot(data=sampled_data[np.logical_or(sampled_data['Well '] == 3, sampled_data['Well '] == 8)], x='Well ', y='Mean Intensity 488nm')
plt.show()

sns.boxplot(data=sampled_data[np.logical_or(sampled_data['Well '] == 4, sampled_data['Well '] == 9)], x='Well ', y='Mean Intensity 488nm')
plt.show()

sns.boxplot(data=sampled_data[np.logical_or(sampled_data['Well '] == 5, sampled_data['Well '] == 10)], x='Well ', y='Mean Intensity 488nm')
plt.show()

sns.boxplot(data=sampled_data[np.logical_or(sampled_data['Well '] == 6, sampled_data['Well '] == 11)], x='Well ', y='Mean Intensity 488nm')
plt.show()

# calculate t test and p value

w2_w7 = stats.ttest_ind(sampled_data[sampled_data['Well '] == 2]['Mean Intensity 488nm'], sampled_data[sampled_data['Well '] == 7]['Mean Intensity 488nm'])
w3_w8 = stats.ttest_ind(sampled_data[sampled_data['Well '] == 3]['Mean Intensity 488nm'], sampled_data[sampled_data['Well '] == 8]['Mean Intensity 488nm'])
w4_w9 = stats.ttest_ind(sampled_data[sampled_data['Well '] == 4]['Mean Intensity 488nm'], sampled_data[sampled_data['Well '] == 9]['Mean Intensity 488nm'])
w5_w10 = stats.ttest_ind(sampled_data[sampled_data['Well '] == 5]['Mean Intensity 488nm'], sampled_data[sampled_data['Well '] == 10]['Mean Intensity 488nm'])
w6_w11 = stats.ttest_ind(sampled_data[sampled_data['Well '] == 6]['Mean Intensity 488nm'], sampled_data[sampled_data['Well '] == 11]['Mean Intensity 488nm'])

print('well 2 vs well 7:')
print('t-statistic: ' + str(w2_w7[0]))
print('p value: ' + str(w2_w7[1]))

print('well 3 vs well 8:')
print('t-statistic: ' + str(w3_w8[0]))
print('p value: ' + str(w3_w8[1]))

print('well 4 vs well 9:')
print('t-statistic: ' + str(w4_w9[0]))
print('p value: ' + str(w4_w9[1]))

print('well 5 vs well 10:')
print('t-statistic: ' + str(w5_w10[0]))
print('p value: ' + str(w5_w10[1]))

print('well 6 vs well 11:')
print('t-statistic: ' + str(w6_w11[0]))
print('p value: ' + str(w6_w11[1]))

