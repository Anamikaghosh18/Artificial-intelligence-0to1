import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

radius = 50
center = (150, 150)
color = (0,0,255)
thickness = -1


if image is not None:
    cv2.circle(image, center, radius , color, thickness)
    cv2.imshow("Circle on image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("OOps!, image loading failed")
