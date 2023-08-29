import os
import numpy as np

#data_path = os.path.join('../data/PeMSD4/pems04.npz')
path = os.getcwd()
data = np.load(path + '/tda_data/PEMSD3_01_MPGrid_Euler_characteristic_degree_sublevel_betweenness_sublevel.npz') #shape is (sequence_length, num_of_vertices, num_of_features)
print(data) # (16992, 307, 3)