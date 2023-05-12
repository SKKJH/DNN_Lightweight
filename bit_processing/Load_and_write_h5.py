import h5py
import numpy as np
import os
import sys
import shutil

filename = sys.argv[1]
bit = sys.argv[2]

filename_write = filename[:-3] + ' (copy).h5'
save_folder = 'saveshift_' + filename


# filename = 'inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5'
# filename_write = 'inception_resnet_v2_weights_tf_dim_ordering_tf_kernels' + '-copy.h5'
# save_folder = 'save_incepRes_origin'

# Open the HDF5 file for reading
with h5py.File(filename, 'r+') as f:
    # Traverse all branches and layers of the file
    def traverse_datasets(name, obj):
        if isinstance(obj, h5py.Dataset):
            # Get the group and dataset names
            group_name, dataset_name = os.path.split(name)

            # print("name: ",name)
            # print("group_name: ", group_name)
            # print("dataset_name: ", dataset_name)

            # Remove the trailing ':0' from the dataset name
            dataset_name_txt = dataset_name[:-2]
            # Convert the dataset to a numpy array and flatten it
            # print("obj: ", obj[()])
            dataset_array = obj[()].flatten()
            # print("flatten obj: ", dataset_array)
            #load txt file
            with h5py.File(filename_write, 'a') as f2:
                write_data = np.loadtxt(f'{save_folder}/{group_name}/{dataset_name_txt}.txt', delimiter='\n')
                # print("write_data: ", write_data.reshape(obj[()].shape))
                # print()
                # print(f2[f'/{group_name}/{dataset_name}'])
                # print(obj[()].shape)
                # print()
                del f2[f'/{group_name}/{dataset_name}']
                f2[f'/{group_name}/{dataset_name}'] = write_data.reshape(obj[()].shape) 


    f.visititems(traverse_datasets)

shifted_h5 = filename_write
shifted_h5_newname = filename[:-3]+ '_' + bit + 'bit.h5'
shutil.copy2(shifted_h5, shifted_h5_newname)
# os.rename(shifted_h5, shifted_h5_newname)
