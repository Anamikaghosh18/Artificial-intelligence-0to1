import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

pt1 = (50,100)
pt2 = (100, 200)
color = (0, 0, 255)
thickness = 5 

if image is not None:
    cv2.rectangle(image, pt1 , pt2 , color, thickness)
    cv2.imshow("Image with Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Oops!! Image load failed.")
