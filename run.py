#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script will grab two directories, one of text files, and another of images
and create a json post request of the information available from the files.

'''

## IMPORT
import os
import re
import json
import requests

## FUNCTIONS
def is_type_file(path, ext):

    '''Returns true if the file passed into the function is of the given extension'''

    basename = os.path.basename(path)
    file_ext = os.path.splitext(basename)[1]

    if file_ext == ext:
        return True
    
    return False


def get_file_name(image_path):

    '''This will return the file name without the extension of file'''
    basename = os.path.basename(image_path)

    return basename


def get_fruit_dict(texts, images):

  text_files_path = os.path.normpath(texts)
  image_files_path = os.path.normpath(images)



  keys = ["name", "weight", "description", "image_name"]

  sorted_txt_list = sorted(os.listdir(text_files_path))
  images = []
  all_images = os.listdir(image_files_path)
  for this_image in all_images:
    if ".jpeg" in this_image:
      images.append(this_image)

  sorted_image_list = sorted(images)

  fruit_list = []

  # Iterate through both the directories
  for text_path, image_path in zip(sorted_txt_list, sorted_image_list):

    this_text_path = os.path.join(text_files_path, text_path)
    this_image_path = os.path.join(image_files_path, image_path)
    
    this_dict = {}

    if is_type_file(this_text_path, ".txt"):

      with open(this_text_path, 'r') as file:
        lines = file.read().splitlines()

        fruit_name = lines[0]

        regex = r"([\d+])"
        result = re.search(regex, lines[1])
        fruit_weight = result.group(1)

        fruit_description = lines[2]
        fruit_description = fruit_description.replace(u'\xa0', u'')


    image_name = get_file_name(this_image_path)

    this_dict[keys[0]] = fruit_name
    this_dict[keys[1]] = int(fruit_weight)
    this_dict[keys[2]] = fruit_description
    this_dict[keys[3]] = image_name

    fruit_list.append(this_dict)

  return fruit_list


def post_fruit(list, url):

    headers = {'Content-Type': 'application/json'}

    '''Return the status code of post request to a given url with the data set from a dictionary'''
    for dictionary in list:
        print(dictionary)
        json_object = json.dumps(dictionary)

        print("Posting to {}".format(url))
        response = requests.post(url=url, data=json_object, headers=headers)

        if response.ok:
            print("Post was good!")

        response.raise_for_status()


def main():

  # Add the directory paths for the texts and images
  text_files = "{}/supplier-data/descriptions".format(os.path.expanduser('~'))
  image_files = "{}/supplier-data/images".format(os.path.expanduser('~'))

  linux_instance = ""
  url = "http://{}/fruits/".format(linux_instance)

  fruit_list = get_fruit_dict(text_files, image_files)

  post_fruit(fruit_list, url)


## RUN
if __name__ == "__main__":
  main()