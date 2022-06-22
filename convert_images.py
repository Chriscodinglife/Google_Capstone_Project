#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script is for the Week 1 Capstone assignment for the Google certification.

This script will do the following:
1. Ask for the location of the folder where the files are being stored.
2. Rotate the image 90 degrees clockwise
3. Resize the image 
4. Save the image in a new folder called .jpeg format

'''

import os
from PIL import Image

## FUNCTIONS

def get_directory():

    '''This function will ask the user for the image folder and return the path of the folder, and the parent folder'''

    given_folder_path = input("Enter the path of the image folder: ").replace('"', "")
    image_folder_path = os.path.normpath(given_folder_path)
    parent_folder_path = os.path.dirname(image_folder_path)

    return image_folder_path, parent_folder_path


def return_image_object(image_path):

    '''This will return an Image/PIL object'''
    image = Image.open(image_path)

    return image


def rotate_image(image, degrees):

    '''This will return an image object that is rotated a given amount of degrees'''
    rotated_image = image.rotate(degrees)

    return rotated_image
    


def resize_image(image, size):

    '''This will return an image object that is resized based on a given size'''
    size_x = size
    size_y = size
    resized_image = image.resize((size_x, size_y))

    return resized_image


def get_file_name(image_path):

    '''This will return the file name without the extension of file'''
    basename = os.path.basename(image_path)
    file_name = os.path.splitext(basename)[0]

    return file_name


def add_tiff_ext(image_path):

    '''This will add the .tiff extension that is missing from a given file'''
    new_file_path = os.path.normpath(image_path + ".tiff")
    
    os.rename(image_path, new_file_path)

    return new_file_path


def convert_image(image, format):

    '''Return an image object in a converted given format'''

    converted_image_object = image.convert(format)
    
    return converted_image_object


def save_image(folder, format, image, file_name):

    '''This will save the image object in a given format in a specific directory and return its path'''

    if format == 'RGB':
        file_ext = ".jpg"
    
    new_image_name = file_name + file_ext
    new_image_path = os.path.join(folder, new_image_name)

    converted_image_object = image.convert(format)

    converted_image_object.save(new_image_path)

    return new_image_path


def main():

    # Get the image path from the user
    image_folder_path, parent_folder = get_directory()

    # Make a new folder for the converted images
    new_path = os.path.normpath("/opt/icons")

    if not os.path.exists(new_path):
        os.mkdir(new_path)
    
    # Iterate through each file in the folder
    for image in os.listdir(image_folder_path):

        # Get the full file path
        image_path = os.path.join(image_folder_path, image)
        # Get the image file name
        image_file_name = get_file_name(image_path)
        # Get the image object
        image_object = return_image_object(image_path)

        # Rotate the image
        rotated_image = rotate_image(image_object, -90)

        # Resize the image
        resized_image = resize_image(rotated_image, 128)

        # Save the new image as a PNG in a new folder
        converted_image_path = save_image(new_path, 'RGB', resized_image, image_file_name)

        print("New image created at: {}".format(converted_image_path))

    
## RUN
if __name__ == "__main__":
    main()