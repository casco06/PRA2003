import numpy as np
import matplotlib.pyplot as plt
# import relevant packages

pbins = np.arange(0, 11, 0.5)
bin_centers = (pbins[:-1] + pbins[1:]) / 2
# make 10 bins for the momenta and get the bin centers for the plot

IDs = [321, -321, 3312, -3312, 211, -211, 3122, -3122, 2212, -2212, 3334, -3334]
# select the ID's


def asymmetry(n_pos, n_neg):
# define a function for asymetry

    total = (n_pos + n_neg).astype(float)
    return np.divide(n_pos - n_neg, total)
# input an ID and its negative and calculate the asymmetry between


def calculate_subsample_asymmetry(filepath):
# define a function for reading a file and calculating the asymmetries

    momenta = {i: [] for i in IDs}
    # create an empty list for each ID
    
    with open(filepath.strip('"'), 'r') as f:
        for line in f:
            elements = line.split()
            if len(elements) < 4 or float(elements[3]) not in IDs:
                continue
    # open the file split the columns and if its less then 3 or the ID isnt entry 4 skip it.

            px, py, pz = (float(x) for x in elements[:3])
            pid = int(float(elements[3]))
            # calculate the momentum and make the ID something we can use in a loop

            momenta[pid].append(np.sqrt(px**2 + py**2 + pz**2))
            # append to momentum and corresponding ID to the list

    counts = {pid: np.histogram(p, bins=pbins)[0] for pid, p in momenta.items()}
    # devide according to momenta bins and calculate the counts

    return (asymmetry(counts[321], counts[-321]), asymmetry(counts[3312], counts[-3312]), asymmetry(counts[211], counts[-211]), asymmetry(counts[3122], counts[-3122]), asymmetry(counts[2212], counts[-2212]), asymmetry(counts[3334], counts[-3334]))
    #  use the prieviously defined asymmetry function on the results

files = [rf'C:\Users\casco\Downloads\output-Set{i}.txt' for i in range(1, 11)]
# list all the files

all_321, all_3312, all_211, all_3122, all_2212, all_3334 = [], [], [], [], [], []
for file in files:
    a321, a3312, a211, a3122, a2212, a3334 = calculate_subsample_asymmetry(file)
    all_321.append(a321)
    all_3312.append(a3312)
    all_211.append(a211)
    all_3122.append(a3122)
    all_2212.append(a2212)
    all_3334.append(a3334)

all_321 = np.array(all_321)
all_3312 = np.array(all_3312)
all_211 = np.array(all_211)
all_3122 = np.array(all_3122)
all_2212 = np.array(all_2212)
all_3334 = np.array(all_3334)
# for every file calculate the asymtries for each bin and append them to the total lists

all_321 = np.array(all_321)
all_3312 = np.array(all_3312)
# convert to arrays 20 columns for each P bin and 10 rows for each file


def mean_and_std(data):
    mean = np.nanmean(data, axis=0)
    sem = np.nanstd(data, axis=0, ddof=1)
    return mean, sem
# return the mean and standard deviation  for each momentum bin nan to protect for 0/0 situations


means_321, std_321 = mean_and_std(all_321)
means_3312, std_3312 = mean_and_std(all_3312)
means_211, std_211 = mean_and_std(all_211)
means_3122, std_3122 = mean_and_std(all_3122)
means_2212, std_2212 = mean_and_std(all_2212)
means_3334, std_3334 = mean_and_std(all_3334)
# calculate the values


def plot_asymmetry(means, sems, label):
    plt.figure()
    plt.errorbar(bin_centers, means, yerr=sems, fmt='o', capsize=3)
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.xlim(0, max(bin_centers) + 1)
    plt.xlabel(r'Momentum ($10^{-23}$ kg m/s)')
    plt.ylabel(rf'Asymmetry (N$_{{{label}}}$ - N$_{{-{label}}}$) / (N$_{{{label}}}$ + N$_{{-{label}}}$)')
    plt.title(rf'Momentum-dependent asymmetry between {label} and -{label}')
    plt.grid()
    plt.show()
# plot the asymmetry with specified labels and data points


plot_asymmetry(means_321, std_321, '321')
plot_asymmetry(means_3312, std_3312, '3312')
plot_asymmetry(means_211, std_211, '211')
plot_asymmetry(means_3122, std_3122, '3122')
plot_asymmetry(means_2212, std_2212, '2212')
plot_asymmetry(means_3334, std_3334, '3334')