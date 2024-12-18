import os 
import numpy as np

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror'

data = np.full((21, 21, 21, 10, 2), -1)

exp_types = ['BR', 'BY', 'RB', 'RY', 'YB', 'YR']

for exp in exp_types : np.save(os.path.join(FOLDER, f'data_{exp}.npy'), data)