import cv2

image = cv2.imread("C:\Desktop\Anamika\8bbc3db5-2718-4ad1-b50d-16d099ee3355.jpg")

'''
(3,3) : light blur 
(9,9) : strong blur 
(21,21) : super blur 

'''

# (3,3) -> the opencv will take the center pixel by blending with neighbour pixels


blurred = cv2.GaussianBlur(image , (3,3), 3)

cv2.imshow("Original image", image)
cv2.imshow("Blurred iamge", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()