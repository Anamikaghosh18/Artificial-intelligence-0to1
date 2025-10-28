# to clean the images if there is noise in the image 

import cv2 

image = cv2.imread(r"C:\Desktop\Anamika\8bbc3db5-2718-4ad1-b50d-16d099ee3355.jpg")

blurred = cv2.medianBlur(image , 5)

cv2.imshow("Original image", image)
cv2.imshow("Cleaned image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()