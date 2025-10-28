import cv2

image = cv2.imread(r'C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg')


if image is not None :
    cv2.imshow("Image showing ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if image is not None:
    success = cv2.imwrite("output_python.jpg", image)
    if success:
        print("Image saved successfully.")
    else:
        print('Error occurred.failed to save.')
else:
    print("Could not load the image")
