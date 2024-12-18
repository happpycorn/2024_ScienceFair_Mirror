import os 
import numpy as np

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror'

FILE_NAME = r'FinishData\data_4.npy'

origin_data = np.load(os.path.join(FOLDER, FILE_NAME))

exp_types = ['BR', 'BY', 'RB', 'RY', 'YB', 'YR']

def findID(data):

    ID_str = f"{data["ID"]:06d}"

    real_ID = tuple(int(ID_str[i:i+2]) for i in range(0, 6, 2)) # w, l, r

    return real_ID

def Histograms(data, num_bins=20):

    min_val, max_val = min(data), max(data)

    bins = np.linspace(min_val, max_val, num_bins + 1)

    hist, bin_edges = np.histogram(data, bins=bins)

    most_popular_idx = np.argmax(hist)
    most_popular_range = (bin_edges[most_popular_idx], bin_edges[most_popular_idx + 1])

    for i, value in enumerate(data):

        if most_popular_range[0] <= value < most_popular_range[1] : return i, most_popular_range[1]

for exp_type in exp_types:

    preprocess_data = np.load(os.path.join(FOLDER, f'PreprocessData\\data_{exp_type}.npy'))

    for row in origin_data:

        w, l, r = findID(row)

        for i in range(10):

            index, stay_point = Histograms(row[exp_type][i])

            preprocess_data[r][l][w][i][0] = index
            preprocess_data[r][l][w][i][1] = stay_point

    np.save(os.path.join(FOLDER, f'PreprocessData\\data_{exp_type}.npy'), preprocess_data)