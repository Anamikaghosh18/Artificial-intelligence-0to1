import cv2

image = cv2.imread(r'C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg'); 

# to load the image 
if image is None:
    print("Error: Image not found");
else:
    print("Image loaded successfully");





