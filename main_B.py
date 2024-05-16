import mne
from matplotlib import pyplot as plt
from scipy.signal import welch


def main():
    raw_data = mne.io.read_raw_snirf("replace with your snrif file",
                                     preload=True)  # loads the raw data in a variable
    sample_frequency = raw_data.info["sfreq"]  # gets the sample frequency from the metadata of the snirf file
    channel_names = raw_data.ch_names
    raw_data = mne.preprocessing.nirs.optical_density(raw_data)
    # Calculate the PSD for each channel (wavelength) through a loop
    for i, ch_name in enumerate(channel_names):
        data = raw_data.get_data(picks=[i])[0]  # Extract data for the i-th channel
        frequencies, psd = welch(data, sample_frequency)
        plt.semilogy(frequencies, psd, label=f'Channel {ch_name}')  # Plot PSD for the i-th channel
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD')
    plt.title('Power Spectral Density (PSD) for All Channels')
    plt.legend()  # Show legend with channel names
    plt.show()  # Display the plot


if __name__ == '__main__':
    main()
