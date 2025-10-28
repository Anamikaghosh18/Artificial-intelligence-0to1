import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

color = (0,0,255)
scale = 1.0

if image is not None:
    cv2.putText(image , "Python Logo",(10,100), cv2.FONT_HERSHEY_SIMPLEX, scale, color, 2)
    cv2.imshow("Image with text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Oops!! No image loaded.")
