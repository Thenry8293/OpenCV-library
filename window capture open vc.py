import cv2 as cv
import numpy as np
import os
from time import time
from window_capture_function import WindowCapture


wincap = WindowCapture('osu!')







loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    
    cv.imshow('Computer vision', screenshot)

    print('FPS: ', 1/(time()-loop_time))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break



print('Done')