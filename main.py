import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Component Infos
manufacturer = ""
manufacturer_part_number = ""
footprint = ""
product_package_type = ""
part_pdf_link = ""
manufacturer_website = ""
excepted_day_of_usage = ""


sender = os.dotenv("YOUR_EMAIL")
receiver = "haidy@easyeda.com"
password = os.getenv("PASSWORD")
subject = "new part require"
body = """Manufacturer: Maxim
Manufacturer part number: MAX861ESA+T
Footprint: SOIC-8
Product package type: tape
Part pdf links(or pdf file): 
manufacturer website: https://www.analog.com/en/index.html
It is expected to be used in days:  """
 #header 

message = """ From: {sender}
 To: {Receiver}
 Subject: {subject}\n
 {body}
 """

server =  smtplib.SMTP("smtp.gmail.com",  587)
server.starttls()
manufacturer = input("\033[1; 32; 40m\Manufacturer: \n")
manufacturer_part_number = input("\033[1; 32; 40m\Manufacturer Part Number:\n ")
footprint = input("\033[1; 32; 40m\Footprint:\n ")
part_pdf_link = input("\033[1; 32; 40m\Part PDF Link: \n")
manufacturer_website = input("\033[1; 32; 40m\Manufacturer Website:\n ")
excepted_day_of_usage = input("\033[1; 32; 40m\When do you except to use it?\n")
try:
    server.login(sender, password)
    print("Logged In...")
    server.sendmail(sender, receiver, message)
    print("Part requested")
except smtplib.SMTPAuthenticationError:
    print("Unable to log in")
    print('Please, make sure you have turned on the setting "Less Secure App Access" on your gmail account')  