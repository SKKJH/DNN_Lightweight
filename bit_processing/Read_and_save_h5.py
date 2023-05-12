import h5py
import numpy as np
import os
import sys

# filename = 'inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5'

filename = sys.argv[1]
save_folder = 'saveorigin_' + filename

# Open the HDF5 file for reading
with h5py.File(filename, 'r') as f:
    # Traverse all branches and layers of the file
    def traverse_datasets(name, obj):
        if isinstance(obj, h5py.Dataset):
            # Get the group and dataset names
            group_name, dataset_name = os.path.split(name)
            # Remove the trailing ':0' from the dataset name
            dataset_name = dataset_name[:-2]
            # Convert the dataset to a numpy array and flatten it
            dataset_array = obj[()].flatten()
            # Create the folder for the group if it doesn't exist
            if not os.path.exists(f'{save_folder}/{group_name}'):
                os.makedirs(f'{save_folder}/{group_name}')
            # Save the flattened array as a text file with the group and dataset name
            np.savetxt(f'{save_folder}/{group_name}/{dataset_name}.txt', dataset_array)
                
    f.visititems(traverse_datasets)
