import cv2 

image = cv2.imread("C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

pt1 = (50, 100)
pt2 = (150, 100)
color = (0,0,255)
thickness = 4

if image is not None:
    cv2.line(image ,pt1 , pt2, color, thickness)
    cv2.imshow("Line drawn", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Oops !! image loading failed")

