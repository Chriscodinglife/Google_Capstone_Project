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
import socket


## FUNCTIONS
def check_cpu_usage(max_percent):

    """Returns True if the cpu percentage if over a given treshold, False otherwise"""
    cpu_usage = psutil.cpu_percent(interval=0.5)

    if cpu_usage > max_percent:
        return True
    return False


def check_cpu_full():

    "Returns True if the CPU is being utilized heavily"
    return check_cpu_usage(max_percent=80)


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


def check_ram_usage(min_ram_available):

    """Returns True if the RAM available is below a certain amount, False Otherwise"""
    available_memory = int(psutil.virtual_memory().available) / 1024 / 1024

    if available_memory < min_ram_available:
        return True
    return False


def check_ram_full():

    "Return True if the RAM available is below the the given amount"
    return check_ram_usage(500)


def check_local_host(hostname, ip_address):

    """Return true if the local host name does not resolve to the given IP Address"""
    host_ip_address = socket.gethostbyname(hostname)

    if not host_ip_address == ip_address:
        return True
    return False


def check_local_ip_to_host():

    """Return True if the given local ip does not resolve to the local host"""
    return check_local_host("localhost", "127.0.0.1")


def main():

    checks =[
        (check_cpu_full, "Error - CPU usage is over 80%"),
        (check_root_full, "Error - Available disk space is less than 20%"),
        (check_ram_full, "Error - Available memory is less than 500MB"),
        (check_local_ip_to_host, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]
    everything_ok = True

    subject_line = ""
    for check, msg in checks:
        if check():
            subject_line = msg
            everything_ok = False

    if not everything_ok:
        
        sender = "automation@example.com"
        user = "<enter_user_here>"
        receiver = "{}@example.com".format(user)

        email_body = "Please check your system and resolve the issue as soon as possible."

        email = emails.generate_email(sender, receiver, subject_line, email_body)
        emails.send_email(email)