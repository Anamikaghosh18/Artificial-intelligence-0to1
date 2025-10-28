import cv2 
import numpy as np 

image = cv2.imread("C:\Desktop\Anamika\8bbc3db5-2718-4ad1-b50d-16d099ee3355.jpg")

sharpen_kernal = np.array([
    [0,-1,0],
    [-1,5,-1], 
    [0,-1,0]])

sharpened = cv2.filter2D(image , -1 , sharpen_kernal)

cv2.imshow('original image', image)
cv2.imshow('sharpened image', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()