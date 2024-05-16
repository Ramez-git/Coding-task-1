import glob
import os

import mne
from matplotlib import pyplot as plt


def Calculate_oxy_data(snirf_file):
    raw = mne.io.read_raw_snirf(snirf_file, preload=True)
    raw = mne.preprocessing.nirs.optical_density(raw)
    hbo_data = mne.preprocessing.nirs.beer_lambert_law(raw)
    return hbo_data


def main():
    directory_path = 'snrif_files'
    files = glob.glob(os.path.join(directory_path, "*.snirf"))
    oxy_data_accumulative_list = []
    for file_path in files:
        oxy_data = Calculate_oxy_data(file_path)
        oxy_data_accumulative_list.extend(oxy_data.get_data())  # Accumulate oxy data from all files
    plt.hist(oxy_data_accumulative_list, bins=50, color='blue', edgecolor='black')  # Plot histogram for all data
    plt.xlabel('Oxyhemoglobin Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Oxyhemoglobin Values')
    plt.show()


if __name__ == '__main__':
    main()
