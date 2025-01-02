import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Component Infos
manufacturer = ""
manufacturer_part_number = ""
footprint = ""
product_package_type = ""
part_pdf_link = ""
manufacturer_website = ""
excepted_day_of_usage = ""


sender = os.getenv("YOUR_EMAIL")
receiver = ""
password = os.getenv("PASSWORD")
subject = "New Part Require"
body = """"""
 #header 


print(sender)
print(password)
server =  smtplib.SMTP("smtp.gmail.com",  587)
server.starttls()
manufacturer = input(f"{bcolors.HEADER}{bcolors.BOLD  }Manufacturer:{bcolors.ENDC} \n")
manufacturer_part_number = input(f"{bcolors.HEADER}{bcolors.BOLD}Manufacturer Part Number: {bcolors.ENDC} \n")
footprint = input(f"{bcolors.HEADER}{bcolors.BOLD}Footprint: {bcolors.ENDC}\n ")
product_package_type = input(f"{bcolors.HEADER}{bcolors.BOLD}Product Package Type: {bcolors.ENDC}\n ")
part_pdf_link = input(f"{bcolors.HEADER}{bcolors.BOLD}Part PDF Link: {bcolors.ENDC} \n")
manufacturer_website = input(f"{bcolors.HEADER}{bcolors.BOLD}Manufacturer Website: {bcolors.ENDC}\n ")
expected_day_of_usage = input(f"{bcolors.HEADER}{bcolors.BOLD}When do you except to use it? {bcolors.ENDC}\n")
body = f"""Manufacturer: 
Manufacturer part number: {manufacturer_part_number}
Footprint: {footprint}
Product package type: {product_package_type}
Part pdf links(or pdf file): {part_pdf_link}
manufacturer website: {manufacturer_website}
It is expected to be used in days: {expected_day_of_usage} """
message = f""" From: {sender}
 To: {receiver}
 Subject: {subject}\n
 {body}
 """
try:
    server.login(sender, password)
    print("Logged In...")
    server.sendmail(sender, receiver, message)
    print("Part requested")
except smtplib.SMTPAuthenticationError:
    print("Unable to log in")
    print('Please, make sure your email and password are correct')
server.quit()