import configparser
import os
import smtplib
import pathlib
import sys
from email.message import EmailMessage
from dotenv import load_dotenv
from pathlib import Path
config = configparser.ConfigParser()
load_dotenv()

home =  pathlib.Path.home()

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


email = ""
password = ""

home = Path.home()
documents = home / "Documents"
config_path = documents / ".easy-eda-part-requester-config.cfg"

def config_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
    return False
home = Path.home()
documents = Path.home() / 'Documents'
def config_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
        else:
            return False
if config_file('.easy-eda-part-requester-config.cfg', documents) == False:

    email = input("Your email: ")
    password = input("Your password: ")

    with open(config_path, "w") as file:
        file.write(f"""[Gmail Credentials]
    YOUR_EMAIL={email}
    YOUR_PASSWORD={password}
            """)
        file.close()
    print(f"Success, Credentials saved successfully!")

# Component Infos
manufacturer = ""
manufacturer_part_number = ""
footprint = ""
product_package_type = ""
part_pdf_link = ""
manufacturer_website = ""
excepted_day_of_usage = ""
if config_file(".easy-eda-part-requester-config.cfg", documents):
    try:
        config.read(documents/'.easy-eda-part-requester-config.cfg')
    except:
        print("Failed to find the config file")
sender = config["Gmail Credentials"]["YOUR_EMAIL"]
receiver = "haidy@easyeda.com"
password = config["Gmail Credentials"]["YOUR_PASSWORD"]
subject = "New Part Require"
body = """"""
 #header 


print(sender)
print(password)
server =  smtplib.SMTP("smtp.gmail.com",  587)
server.starttls()
try:
    manufacturer = input(f"{Bcolors.HEADER}{Bcolors.BOLD  }Manufacturer:{Bcolors.ENDC} \n")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    manufacturer_part_number = input(f"{Bcolors.HEADER}{Bcolors.BOLD}Manufacturer Part Number: {Bcolors.ENDC} \n")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    footprint = input(f"{Bcolors.HEADER}{Bcolors.BOLD}Footprint: {Bcolors.ENDC}\n ")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    product_package_type = input(f"{Bcolors.HEADER}{Bcolors.BOLD}Product Package Type: {Bcolors.ENDC}\n ")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    part_pdf_link = input(f"{Bcolors.HEADER}{Bcolors.BOLD}Part PDF Link: {Bcolors.ENDC} \n")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    manufacturer_website = input(f"{Bcolors.HEADER}{Bcolors.BOLD}Manufacturer Website: {Bcolors.ENDC}\n ")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()
try:
    expected_day_of_usage = input(f"{Bcolors.HEADER}{Bcolors.BOLD}When do you except to use it? {Bcolors.ENDC}\n")
except KeyboardInterrupt:
    print("Quitting...")
    exit()
    server.quit()

server =  smtplib.SMTP("smtp.gmail.com",  587)
server.starttls()
body = f"""
Hey i'd like to request a part, here the all the details:
Manufacturer: {manufacturer} 
Manufacturer part number: {manufacturer_part_number}
Footprint: {footprint}
Product package type: {product_package_type}
Part pdf links(or pdf file): {part_pdf_link}
manufacturer website: {manufacturer_website}
It is expected to be used in days: {expected_day_of_usage} """
msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver
try:
    server.login(sender, password)
    server.send_message(msg)
    print(f"{Bcolors.OKGREEN}{ Bcolors.BOLD}Success", "Part requested successfully!")
except smtplib.SMTPAuthenticationError:
    print(f"{Bcolors.FAIL}{Bcolors.BOLD}Error", "Unable to log in. Please, make sure your email and password are correct. {bcolors.ENDC}")
server.quit()