#!/usr/bin/python3
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:

    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= red_mask)
    
    cv2.imshow('result',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
