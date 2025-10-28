import cv2 

image = cv2.imread('C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg')

if image is not None:
    cropped = image[100:200, 50:150] # [start_y : end_y , start_x , end_x]

    cv2.imshow("Original image", image)
    cv2.imshow("cropped image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
