#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script will generate a pdf based on a given set of text file data

'''
## IMPORT
import os
from datetime import date
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

## FUNCTIONS

def generate_report(filename, title, additional_info):

    "Build out the report and save the file"

    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info])


def todays_date():

    '''Return the current date'''

    today = date.today()

    today_formatted = today.strftime("%B %d, %Y")

    return today_formatted


def is_type_file(path, ext):

    '''Returns true if the file passed into the function is of the given extension'''

    basename = os.path.basename(path)
    file_ext = os.path.splitext(basename)[1]

    if file_ext == ext:
        return True
    
    return False


def get_text_dict(text):

    text_files_path = os.path.normpath(text)

    keys = ["name", "weight"]

    text_list = os.listdir(text_files_path)

    this_list = []

    # Iterate through both the directories
    for text_path in text_list:
        
        this_dict = {}

        if is_type_file(text_path, ".txt"):

            with open(text_path, 'r') as file:
                lines = file.read().splitlines()

                fruit_name = lines[0]
                fruit_weight = lines[1]

            this_dict[keys[0]] = fruit_name
            this_dict[keys[1]] = fruit_weight

            this_list.append(this_dict)

    return this_list
