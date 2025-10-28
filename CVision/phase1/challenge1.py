'''

- take the input from the user 
- change the image to grayscale 
- ask the user whether want to show or save the iamge 
- if want to save the image then take the name 

'''

import cv2

path = input("Give the image path: ")

print("Your image path is: ", path)

# load the path 
image = cv2.imread(path)

# check the image is loaded successfully or not 
if image is not None:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    choice = input("what you want to do:\n 1. Show \n 2. Save \n Choose 1 or 2 \n Choose: ")

    # what the user want to do  
    if(choice == "1"):
        cv2.imshow("image: ", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(choice == "2"):
        output_img_name = input("provide the output image name: ")
        saved_img = cv2.imwrite(output_img_name, gray_img)
        print(f"Grayscale image saved: {saved_img}")

    else:
        print("Invalid choose from above option")

else:
    print("Error: Image doesnot loaded.")
