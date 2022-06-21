#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script is for the week 2 of the Google IT Automation Python Certificate

This will do the following:
1. Iterate through the text files inside a folder
2. Parse the contents of each file and convert them into a dictionary
3. Take each dictionary and make a post request to a specific URL

'''

import os
import json
import requests


## FUNCTIONS

def is_text_file(path):

    '''Returns true if the file passed into the function is a text file'''

    basename = os.path.basename(path)
    file_ext = os.path.splitext(basename)[1]

    if file_ext == ".txt":
        return True
    
    return False


def texts_to_list(list):

    '''Return a list of dictionary objects'''

    this_list = []

    keys = ["title", "name", "date", "feedback"]

    for file_path in list:

        if is_text_file(file_path):

            this_dict = {}
            with open(file_path, 'r') as file:
                lines = file.read().splitlines()

            x = 0
            for line in lines:
                this_dict[keys[x]] = line
                x += 1

            this_list.append(this_dict)
    
    return this_list


def post_message(list, url):

    headers = {'Content-Type': 'application/json'}

    '''Return the status code of post request to a given url with the data set from a dictionary'''
    for dictionary in list:
        json_object = json.dumps(dictionary)

        print("Posting to {}".format(url))
        response = requests.post(url=url, data=json_object, headers=headers)

        if response.ok:
            print("Post was good!")

        response.raise_for_status()


def main():

    directory = '/data/feedback'
    web_address = "<enter_host_domain_here"
    post_url = "http://{}/feedback/".format(web_address)

    # Get the normalized path for a given directory
    this_directory = os.path.normpath(directory)

    list_of_files = []
    # Iterate through each file in the given path
    for file in os.listdir(this_directory):

        this_file_path = os.path.join(this_directory, file)
        list_of_files.append(this_file_path)

    dict_list = texts_to_list(list_of_files)
    post_message(dict_list, post_url)


## RUN
if __name__ == "__main__":
    main()