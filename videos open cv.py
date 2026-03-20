import numpy as np
import cv2 as cv
import os

def videoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()
    
    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows

def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'demoImages\\TrimmedclipfromFeb222025.mp4')
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(5)
        if cv.waitKey(delay) == ord('q'):
            break




if __name__ == '__main__':
    # videoFromWebcam()
    videoFromFile()
   