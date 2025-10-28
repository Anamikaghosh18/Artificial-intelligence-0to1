import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

if image is None :
    print("Error: Image not loaded")
else:
    print('Image loaded successfully')

if image is not None:
    cv2.imshow("Image showing: ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not loaded successfully")