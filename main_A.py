import matplotlib.pyplot as plt
import mne
import numpy as np
from scipy.signal import welch


def SCI_value_calculation(raw_data):
    """Function to calculate the Scalp Coupling Index value from raw data."""
    sci = mne.preprocessing.nirs.scalp_coupling_index(raw_data)
    return sci


def PSP_value_calculation(raw_data, sampling_frequancy, frequancy_band=(0.01, 0.2)):
    """function to calculate the PSP value from raw data."""
    psp_values = []
    for channel_data in raw_data.get_data():
        f, Pxx = welch(channel_data, fs=sampling_frequancy, nperseg=1024)
        freq_mask = (f >= frequancy_band[0]) & (f <= frequancy_band[1])
        band_power = np.sum(Pxx[freq_mask])
        psp_values.append(band_power)
    return np.array(psp_values)


def main():
    raw_data = mne.io.read_raw_snirf("replace_with_path_to_your_snirf_file",
                                     preload=True)  # loads the raw data in a variable
    sample_frequency = raw_data.info["sfreq"]  # gets the sample frequency from the metadata of the snirf file
    n_channels = len(raw_data.ch_names)  # counts the number of channels
    sci_values = SCI_value_calculation(raw_data)  # calculates the SCI
    psp_values = PSP_value_calculation(raw_data, sample_frequency)  # calculates the PSP
    # starts making the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    width = 0.35
    indices = np.arange(n_channels)
    ax.bar(indices - width / 2, sci_values, width, label='SCI')
    ax.bar(indices + width / 2, psp_values, width, label='PSP')
    ax.set_xlabel('Channels')
    ax.set_ylabel('Values')
    ax.set_title('Comparison of SCI and PSP Values')
    ax.set_xticks(indices)
    ax.set_xticklabels(raw_data.ch_names, rotation=90)
    ax.legend()
    plt.tight_layout()
    # displays the plot
    plt.show()


if __name__ == '__main__':
    main()
