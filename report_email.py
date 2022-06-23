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
import reports


## FUNCTIONS

def main():

    today = reports.todays_date()
    title = "Processed Update on {}".format(today)

    text_files = "~/supplier-data/descriptions"
    text_list = reports.get_text_dict(text_files)

    summary_pdf_body = ""
    for dict in text_list:
        summary_pdf_body += "<br/>"
        dict_values = dict.items()
        sorted_values = sorted(dict_values)
        for key, value in sorted_values:
            summary_pdf_body += key + ": " + value
        summary_pdf_body += "<br/>"

    report_file_name = "/tmp/processed.pdf"
    reports.generate_report(report_file_name, title, summary_pdf_body)


## RUN

if __name__ == "__main__":
    main()