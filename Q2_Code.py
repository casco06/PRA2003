import pandas as pd
import numpy as np
# import the packages needed

df = pd.read_csv('total_data.csv')
df.columns = ['ID', 'Freq', 'Mean', 'STD']
# read the csv file as a pandas dataframe and rename the columns

for i in df['ID'].unique():
# for every unique ID:

    subset = df[df['ID'] == i]
    # a subset is the list of all ID's that are i

    total_mean = np.average(subset['Mean'], weights=subset['Freq'])
    total_sigma = np.std(subset['Mean'])
    # the total average is the average of the mean columns with freq as weights
    # the toal sigma is the std of the submeans

    print(f'{i}: {total_mean} +/- {total_sigma}')
    # print the results

for i in df['ID'].unique():
    # for unique ID's
    
    if i > 0 and -i in df['ID'].values:
    # if the ID is positive

        antisubset = df[df['ID'] == -i]
        subset = df[df['ID'] == i]
        # the anti is the negative version the subset is the positive

        n = min(len(subset), len(antisubset))
        # n is the length used for the ammount of elements in the column (i.e if 211 occurs 10 times but -211 9 times compare 9)

        mean_sub_differences = abs(subset['Mean'].values[:n] - antisubset['Mean'].values[:n])
        # take all the differences of the means between the -i and i ID's

        total_mean_difference = np.mean(mean_sub_differences)
        total_sigma_difference = np.std(mean_sub_differences)
        # calculate STD and Mean

        print(f'{i} vs {-i}: Significant within: {round(abs(total_mean_difference/total_sigma_difference), 3)} σ')