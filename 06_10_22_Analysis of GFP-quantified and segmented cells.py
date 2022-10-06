import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# load raw data file
folder_path = r"C:\Users\zoharga\Desktop\Zohar\141121 Emma analysis - Analysis of GFP-quantified and segmented cells\061022"
data = pd.read_csv(os.path.join(folder_path, 'ParameterData_Main.txt'), sep='\t')

# remove cells out of gate (ROI)
data = data[data['R01'] == 1].reset_index(drop=True)

# rename wells according to wanted comparisons
# The pics to use and compare against each other are: s1-4 (strain 1) and s145-148 (strain 2)
strains_dict = {1: 1, 2: 1, 3: 1, 4: 1,
                145: 2, 146: 2, 147: 2, 148: 2}
# remove unwanted wells for the data
data = data[data['Well '].isin(list(strains_dict.keys()))]
data['Strain'] = data['Well '].replace(strains_dict)

# sample 500 cells from each wanted well (1-4, 145-148) and export data
sampled_data_500 = pd.DataFrame()
for s in [1, 2]:
    sampled_data_500 = pd.concat([sampled_data_500, data[data['Strain'] == s].sample(n=500)])
# export data for plotting to csv
sampled_data_500.to_csv(os.path.join(folder_path, 'sampled data - 500 cells per strain.csv'), index=False)

# sample 100 cells from each wanted well (1-4, 145-148) and export data
sampled_data_100 = pd.DataFrame()
for s in [1, 2]:
    sampled_data_100 = pd.concat([sampled_data_100, data[data['Strain'] == s].sample(n=100)])
# export data for plotting to csv
sampled_data_100.to_csv(os.path.join(folder_path, 'sampled data - 100 cells per strain.csv'), index=False)

# plot
# s1-4 (Strain 1) vs s145-148 (Strain 2)
# 500 samples
sns.boxplot(data=sampled_data_500[np.logical_or(sampled_data_500['Strain'] == 1, sampled_data_500['Strain'] == 2)],
            x='Strain', y='Mean Intensity 488nm').set(title='Strain 1 vs. Strain 2 - 500 sampled cells')
plt.show()
# 100 samples
sns.boxplot(data=sampled_data_100[np.logical_or(sampled_data_100['Strain'] == 1, sampled_data_100['Strain'] == 2)],
            x='Strain', y='Mean Intensity 488nm').set(title='Strain 1 vs. Strain 2 - 100 sampled cells')
plt.show()

# calculate t test and p value
# s1-4 (Strain 1) vs s145-148 (Strain 2)
# 500 samples
s1_s2_500 = stats.ttest_ind(sampled_data_500[sampled_data_500['Strain'] == 1]['Mean Intensity 488nm'],
                        sampled_data_500[sampled_data_500['Strain'] == 2]['Mean Intensity 488nm'])

print('Strain 1 (s1-4) vs. Strain 2 (s145-148) - 500 cells sampled:')
print('t-statistic: ' + str(s1_s2_500[0]))
print('p value: ' + str(s1_s2_500[1]))

# 100 cells samples
s1_s2_100 = stats.ttest_ind(sampled_data_100[sampled_data_100['Strain'] == 1]['Mean Intensity 488nm'],
                        sampled_data_100[sampled_data_100['Strain'] == 2]['Mean Intensity 488nm'])

print('Strain 1 (s1-4) vs. Strain 2 (s145-148) - 100 cells sampled:')
print('t-statistic: ' + str(s1_s2_100[0]))
print('p value: ' + str(s1_s2_100[1]))
