#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 23:21:58 2017

@author: johnkenny
"""

import numpy as np
import cv2

#==============================================================================
# import as follows conda install -c menpo opencv3
#==============================================================================

"""
dummp func
"""
def dummy(val):
    pass
#filters
idKernel = np.array([
        [0,0,0],
        [0,1,0],
        [0,0,0]])
box = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]], np.float32)/9
sharpen = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]])
    
gaussian = cv2.getGaussianKernel(3,0)
gaussian2 = cv2.getGaussianKernel(5,0)
    
    
kernels = [idKernel, sharpen, gaussian, gaussian2]




#creates the UI window to add all UI elements
cv2.namedWindow('filterapp')

#import image
image = cv2.imread("mj.jpg")
#copy of image to edit
modify = image.copy()


#grayscaling
original_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mod_gray = original_gray.copy()

# tractbars
cv2.createTrackbar("contrast", "filterapp", 1, 100, dummy)
cv2.createTrackbar("brightness", "filterapp", 50, 100, dummy)
cv2.createTrackbar("filter", "filterapp", 0, len(kernels)-1, dummy)
cv2.createTrackbar("grayscale", "filterapp", 0, 1, dummy)

imagecouter = 1
#run until the q key is pressqedw
while True:
    #check grayscale
    grayscale = cv2.getTrackbarPos("grayscale", "filterapp")
    #waits for a key press sets it to k returns num value of key
    key = cv2.waitKey(1) & 0xFF
    # if k is equal to the num val of the q key
    if key == ord("q"):
        break
    #save image on s press
    elif key == ord("s"):
        if grayscale == 1:
            cv2.imwrite("output%d.png" % imagecouter, mod_gray)
        else:
             cv2.imwrite("output%d.png" % imagecouter, modify)
        imagecouter = imagecouter + 1
    #get contrst value
    contrast = cv2.getTrackbarPos("contrast", "filterapp")
    #get brightness value
    brightness = cv2.getTrackbarPos("brightness", "filterapp")
    #get filter kernel index
    filterIn = cv2.getTrackbarPos("filter", "filterapp")
    
    
    #select whick image to display (gray or colour)
    if grayscale == 1:
        #show image
        cv2.imshow("filterapp", mod_gray)
    else:
        #show image
        cv2.imshow("filterapp", modify)
    
    #set the filter kernel
    modify = cv2.filter2D(image, -1, kernels[filterIn])
    mod_gray = cv2.filter2D(original_gray, -1, kernels[filterIn])
    #print(kernels[filterIn])
    
    #add contrast
    modify = cv2.addWeighted(modify, contrast, np.zeros(image.shape, dtype = image.dtype), 0, brightness-50)
    mod_gray = cv2.addWeighted(mod_gray, contrast, np.zeros(original_gray.shape, dtype = original_gray.dtype), 0, brightness-50)
    
cv2.destroyAllWindows()
cv2.waitKey(1) 
        
