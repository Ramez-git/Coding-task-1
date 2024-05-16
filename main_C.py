import glob
import os
import mne
from matplotlib import pyplot as plt


def Calculate_oxy_data(raw_ob):
    """Function to calculate oxy data"""
    hbo_data = mne.preprocessing.nirs.beer_lambert_law(raw_ob)
    return hbo_data.get_data()


def main():
    directory_path = 'replace with snirf files directory'  # gets the snrif files for processing
    files = glob.glob(os.path.join(directory_path, "*.snirf"))  # gets only snirf files from the folder
    # making variables
    oxy_data_transpose = []
    raw_times = []
    raw = None
    # loop that goes through every file
    for file_path in files:
        # gathering data in lists to plot
        raw = mne.io.read_raw_snirf(file_path, preload=True)
        raw = mne.preprocessing.nirs.optical_density(raw)
        oxy_data_transpose.extend(Calculate_oxy_data(raw).T)
        raw_times.extend(raw.times)
    # plotting the data
    plt.plot(raw_times, oxy_data_transpose)
    plt.xlabel('Time (s)')
    plt.ylabel('HbO Concentration (AU)')
    plt.title('Oxyhemoglobin (HbO) Concentration')
    plt.show()


if __name__ == '__main__':
    main()
