import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    cv2.imshow("GrayScale image: ", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")

cv2.imwrite('grayImage.jpg', image)


