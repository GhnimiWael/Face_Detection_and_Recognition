#!/bin/bash

# Set the source and destination directories
src_dir="/opt/projects/face_recon/VIDTIMITtrain"
dest_dir="/opt/projects/face_recon/database"

# Create the destination folder if it doesn't exist
mkdir -p "$dest_dir"

# Loop through all subfolders in the source directory
for subfolder in "$src_dir"/s*; do
    # Extract the digit from the subfolder name (e.g., s1 -> 1)
    user_num="${subfolder##*s}"

    # Loop through each picture in the subfolder
    for picture in "$subfolder"/*.jpg; do
        # Extract the picture number (e.g., /opt/projects/face_recon/dataset/s1/1.pgm -> 1)
        pic_num="${picture##*/}"

        # Copy and rename the picture to the destination folder
        cp "$picture" "$dest_dir/User.$user_num.$pic_num"
    done
done

echo "Copying and renaming complete!"

