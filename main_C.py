import glob
import os

import mne
import numpy as np


def Calculate_oxy_data(snirf_file):
    raw = mne.io.read_raw_snirf(snirf_file, preload=True)
    oxy_indices = [i for i, ch in enumerate(raw.ch_names) if 'hbo' in ch]
    oxy_data = raw.get_data(picks=oxy_indices)
    return oxy_data.flatten()


def main():
    directory_path = 'replace with the path to your directory that has .snrif files'
    files = glob.glob(os.path.join(directory_path, "*.snrif"))
    oxy_data_accumulative_list = []
    for file_path in files:
        oxy_data = Calculate_oxy_data(file_path)
        oxy_data_accumulative_list.append(oxy_data)
    oxy_data_accumulative_list = np.concatenate(oxy_data_accumulative_list)


if __name__ == '__main__':
    main()
