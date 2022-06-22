#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script is for uploading a set of images to a given
url

The script will do the following:
- Iterate through a folder and look for a given format of files (in this case .jpegs)
- Upload each file to a given url using requests
'''

## IMPORT
import os
import requests


## FUNCTIONS

def main():

    image_folder = "~/supplier-data/images"
    image_folder_path = os.path.normpath(image_folder)
    
    web_address = "<enter_address_here>"
    url = "http://{}/upload/".format(web_address)


    # Go through a given folder and look for specific images
    for image in os.listdir(image_folder_path):

        # Get the full path of the image file
        image_path = os.path.join(image_folder_path, image)

        # Get the basename of the file and the extension
        basename = os.path.basename(image_path)
        file_extension = os.path.splitext(basename)[1]

        # Check if the file extension is .jpeg
        if file_extension == ".jpeg":
            with open(image_path, 'rb') as image_file:
                response = requests.post(url, files={'file': image_file})