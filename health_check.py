#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script is designed to raise an alert if there is an issue with the current
machine. If there is an issue, it will send an email so that someone can review
the status of the device

'''

## IMPORT
import os
import sys
import shutil
import psutil
import emails


## FUNCTIONS
def check_disk_full(disk, min_percent):

    """Returns True if there isnt enough disk space, False Otherwise"""
    du = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total

    if percent_free < min_percent:
        return True

    return False


def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_percent=20)


def main():

    checks =[
        (check_root_full, "Root partition full"),
    ]

    for check, msg in checks:
        if check():
            print(msg)

