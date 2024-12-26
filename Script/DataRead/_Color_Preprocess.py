import os 
import numpy as np

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror'

PATH = r'FinishData\Color\data_c6.npy'

def Histograms(data, num_bins=20):

    min_val, max_val = min(data), max(data)

    bins = np.linspace(min_val, max_val, num_bins + 1)

    hist, bin_edges = np.histogram(data, bins=bins)

    most_popular_idx = np.argmax(hist)

    return bin_edges[most_popular_idx + 1]

origin_data : dict = np.load(os.path.join(FOLDER, PATH), allow_pickle=True).item()

data = {key : list(map(Histograms, origin_data[key])) for key in origin_data.keys()}

np.save(os.path.join('data.npy'), data)