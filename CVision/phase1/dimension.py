import cv2 

image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg") 

if image is not None:
    print("Image dimension: ", image.shape)
else:
    print("Image load failed.")