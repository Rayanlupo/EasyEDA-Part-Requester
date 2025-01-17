import configparser
import smtplib
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv

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








# Component Infos
manufacturer = ""
manufacturer_part_number = ""
footprint = ""
product_package_type = ""
part_pdf_link = ""
manufacturer_website = ""
excepted_day_of_usage = ""
if '.config.cfg' not in home:
    with open(home, '.config.cfg') as file:
        file.write("""
        [Gmail Credentials]\n
YOUR_EMAIL=your_email@example.com\n
YOUR_PASSWORD=your_password
        """)
try:
    config.read('.config.cfg')
except:
    print("Failed to find the config file")

sender = config["Gmail Credentials"]["YOUR_EMAIL"]
receiver = "rayanciao09@gmail.com"
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