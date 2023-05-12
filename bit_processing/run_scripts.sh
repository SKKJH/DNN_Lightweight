#!/bin/bash

filename=mask_xception_weights_tf_dim_ordering_tf_kernels.h5

# Execute Read_and_save_h5.py
python3 Read_and_save_h5.py $filename
# Execute extract_txt.py
python3 extract_txt.py $filename

# Execute bit_shift with the specified parameters using a for loop
for i in {32,30,28,26,24,22,20,18,16,14,12,10,8,6,4,2}; do
  # Compile bit_shift.cpp
  g++ -o bit_random bit_random.cpp
  ./bit_random $filename $i 
  # Execute insert_txt_with_directory.py
  python3 insert_txt_with_directory.py $filename

  # Execute Load_and_write_h5.py
  python3 Load_and_write_h5.py $filename $i

  echo $i done.
done
