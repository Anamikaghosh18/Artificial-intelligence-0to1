import cv2

# Correct file path using raw string
image = cv2.imread(r"C:\Desktop\Decoding Ai Eng\CVision\images\python.jpg")

if image is not None:
    print("Image shape:", image.shape)  # Print shape in console

    # Display image
    cv2.imshow("Image", image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close image window
    cv2.destroyAllWindows()
else:
    print("Image not found or invalid path")
   
