import cv2 

image = cv2.imread('C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg')

show = cv2.imshow("Original image", image)

if image is None:
    print("Image load failed")
else:
    print("Image loaded")
    # width , height in a tuple 
    resized = cv2.resize(image ,(300,200))

    cv2.imshow("Resized image", resized)

    cv2.imwrite("resized_img.png", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
