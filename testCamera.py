# Description: Test the camera and display the image

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480) 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    # Press q to quit
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()