#!/usr/bin/env python3

'''
 ______     __  __     ______     __     ______    
/\  ___\   /\ \_\ \   /\  == \   /\ \   /\  ___\   
\ \ \____  \ \  __ \  \ \  __<   \ \ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/ /_/   \/_/   \/_____/ 
                                                   
June 2022

This script will generate a report and send out the report in PDF format
via an email

'''

## IMPORT
import os
import reports
import emails


## FUNCTIONS

def main():

    # Get Today's date
    today = reports.todays_date()
    title = "Processed Update on {}".format(today)

    # Get the list of text files
    text_files = "{}/supplier-data/descriptions".format(os.path.expanduser('~'))
    text_list = reports.get_text_dict(text_files)

    # Create the PDF Body
    summary_pdf_body = ""
    for dict in text_list:
        summary_pdf_body += "<br/>"
        dict_values = dict.items()
        sorted_values = sorted(dict_values)
        for value in sorted_values:
            summary_pdf_body += value[0] + ": " + value[1]
        summary_pdf_body += "<br/>"

    # Create the PDF
    report_file_name = "/tmp/processed.pdf"
    reports.generate_report(report_file_name, title, summary_pdf_body)

    # Prepare the email to be sent
    sender = "automation@example.com"
    user = ""
    receiver = "{}@example.com".format(user)
    subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    # Send email
    email = emails.generate_email(sender, receiver, subject, email_body, report_file_name)
    emails.send_email(email)


## RUN

if __name__ == "__main__":
    main()