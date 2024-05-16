import mne
from matplotlib import pyplot as plt
from scipy.signal import welch


def main():
    raw_data = mne.io.read_raw_snirf("replace_with_path_to_your_snirf_file",
                                     preload=True)  # loads the raw data in a variable
    sample_frequency = raw_data.info["sfreq"]  # gets the sample frequency from the metadata of the snirf file
    channel_names = raw_data.ch_names
    # Calculate the PSD for each channel (wavelength) through a loop
    for i, channel_data in enumerate(raw_data.get_data):
        frequencies, psd = welch(channel_data, sample_frequency)
        # starts creating the plot
        plt.figure()
        plt.semilogy(frequencies, psd)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('PSD')
        plt.title(f'Power Spectral Density (PSD) - Channel {channel_names[i]}')
        # displays the plot
        plt.show()


if __name__ == '__main__':
    main()
