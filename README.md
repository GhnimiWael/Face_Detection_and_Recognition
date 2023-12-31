# Face Detection and Recognition Using Python
Face Detection and Recognition: A GitHub repository showcasing Python and OpenCV-based tools for accurate and efficient face detection and recognition, enabling easy integration into various applications and projects. 📸👤


<p align="center" width="60%">
    <img width="80%"src="https://i.imgur.com/PGgVsyp.png"> 
</p>

## Contents

1. `cascades`: Directory containing pre-trained Haar cascades for face detection.
2. `dataset`: Directory containing face image datasets.
3. `convert_to_gray.py`: Python script to convert images to grayscale.
4. `faceDataset.py`: Python script to collect face datasets from the camera.
5. `faceDetection.py`: Python script for real-time face detection using Haar cascades.
6. `faceRecognition.py`: Python script for face recognition using OpenCV.
7. `faceTraining.py`: Python script for training the face recognition model.
8. `testCamera.py`: Python script to test the camera for face detection.
9. `trainer`: Directory containing the trained model for face recognition.
10. `trainer.zip`: Zip archive of the trained model.
11. `dataset.zip`: Zip archive of face image datasets.
12. `extract_imag_from_db.sh`: This bash script copies and renames pictures from a source directory "/opt/projects/face_recon/VIDTIMITtrain" to a destination directory "/opt/projects/face_recon/database," organizing them by user number and picture number.

## Usage

1. Run `faceDataset.py` to collect face datasets using your camera.
2. Utilize `faceDetection.py` for real-time face detection with Haar cascades.
3. Train the face recognition model with `faceTraining.py`.
4. Use `faceRecognition.py` to recognize faces based on the trained model.
5. For further details, refer to the individual script files.

## Requirement
```bash
pip install -r requirements.txt
```

## Environment Information:
- Python Version: 3.10.6
- Operating System: Ubuntu 22.04.2 LTS x86_64
- Memory: 16 GiB
- CPU: Intel i5-8250U (8) @ 3.400GHz
- GPU: Intel UHD Graphics 620

This environment provides the necessary platform for running Python scripts and performing various tasks involving face detection and recognition using OpenCV and other related libraries. The powerful CPU and sufficient memory ensure smooth execution and efficient processing of image data. The Intel UHD Graphics 620 GPU provides hardware acceleration, if needed, for computationally intensive tasks related to computer vision and deep learning.

## Paper

You can find a detailed paper titled "Face Detection and Recognition Using Python" in the repository. [Download the paper (PDF)](https://github.com/GhnimiWael/Face_Detection_and_Recognition/blob/main/Face%20Detection%20and%20Recognition%20Using%20Python.pdf).

Feel free to explore and use these scripts to enhance your face detection and recognition projects! 📸👤


