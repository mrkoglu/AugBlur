import cv2 
import os 

def apply_gaussian_blur(image, level='high'):
    if level == "low":
        kernel_size = (3,3)
    elif level == "medium":
        kernel_size = (5,5)
    elif level == "high":
        kernel_size = (15,15)
    else:
        print("Invalid blur level. Using default (medium) blur level.")
        kernel_size = (5,5)

    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        raise ValueError("Kernel size should be odd numbers.")
    
    return cv2.GaussianBlur(image, kernel_size, 0)

def copy_txt_file(src_path, dest_path):
    with open(src_path, 'r') as src, open(dest_path, 'w') as dest:
        dest.write(src.read())

def startProcess(inn, out):

    input_folder = "./ornek_resimler"
    output_folder = "./output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if filename.endswith(".jpg"):
            img = cv2.imread(file_path)

           
            blurred_image = apply_gaussian_blur(img)

          
            blurred_filename = "blurred_" + filename
            cv2.imwrite(os.path.join(output_folder, blurred_filename), blurred_image)

            print(f"Blurred version of {filename} has been saved as {blurred_filename}")

        elif filename.endswith(".txt") and filename != "classes.txt":
         
            blurred_txt_filename = "blurred_" + filename
          
            copy_txt_file(file_path, os.path.join(output_folder, blurred_txt_filename))

            ##print(f"Copied annotations from {filename} to {blurred_txt_filename}")
