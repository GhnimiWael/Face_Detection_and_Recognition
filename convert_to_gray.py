import os
import cv2

# Set the source and destination directories
src_dir = "/opt/projects/face_recon/dataset"
dest_dir = "/opt/projects/face_recon/new_dataset"
face_detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')


# Create the destination folder if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Get a list of all files in the source directory
file_list = os.listdir(src_dir)

# Loop through each file in the source directory
for filename in file_list:
    # Check if the file is an image (you may want to add more extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.pgm')):
        # Read the image from the source directory
        img_path = os.path.join(src_dir, filename)
        img = cv2.imread(img_path)

        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_img, 1.3, 5) 

        # Save the grayscale image to the destination directory with the same name
        dest_path = os.path.join(dest_dir, filename)
        cv2.imwrite(dest_path, gray_img)

print("Grayscale conversion and saving complete!")
