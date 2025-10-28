import cv2 

image = cv2.imread("C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

if image is not None:

    (height, width) = image.shape[:2]
    

    center = (height // 2 , width // 2)


    M = cv2.getRotationMatrix2D(center , 90, 1.0) # height // 2 and width // 2 -> we get the intersection as a the center
    rotated_image = cv2.warpAffine(image , M , (height, width))

    flipped_image_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1) # mirror image 


    cv2.imshow("original image", image)
    cv2.imshow("Rotated image", rotated_image)
    cv2.imshow("Flipped vertically", flipped_vertical)
    cv2.imshow("Flipped Horizontally", flipped_image_horizontal)
    cv2.imshow("Flipped Both", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

