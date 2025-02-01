import os
import smtplib

from email.message import EmailMessage

from pathlib import Path
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# Global Variables
email = ""
password = ""

# File Paths
home = Path.home()
documents = home / "Documents"
config_path = documents / ".easy-eda-part-requester-config.cfg"

# Check if config file exists
def config_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
    return False

# Load Credentials
def load_credentials():
    global email, password
    if config_path.exists():
        with open(config_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("YOUR_EMAIL="):
                    email = line.split("=")[1].strip()
                elif line.startswith("YOUR_PASSWORD="):
                    password = line.split("=")[1].strip()

# Save Credentials
def get_credentials():
    global email, password
    email = email_entry.get()
    password = password_entry.get()
    with open(config_path, "w") as file:
        file.write(f"""[Gmail Credentials]
YOUR_EMAIL={email}
YOUR_PASSWORD={password}
        """)
    messagebox.showinfo("Success", "Credentials saved successfully!")
    root.destroy()

# Config Window
if not config_file('.easy-eda-part-requester-config.cfg', documents):
    root = tk.Tk()
    root.title("Config E.E.P.R.")

    tk.Label(root, text="Email:").grid(row=0, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1)

    submit_button = tk.Button(root, text="Save", command=get_credentials)
    submit_button.grid(row=2, columnspan=2)

    root.mainloop()
else:
    load_credentials()

# Main Application Window
root = tk.Tk()
root.title("EasyEDA Part Request")

# Component Infos
manufacturer = ""
manufacturer_part_number = ""
footprint = ""
product_package_type = ""
part_pdf_link = ""
manufacturer_website = ""
excepted_day_of_usage = ""

tk.Label(root, text="Manufacturer:").grid(row=0, column=0)
manufacturer_entry = tk.Entry(root)
manufacturer_entry.grid(row=0, column=1)

tk.Label(root, text="Manufacturer Part Number:").grid(row=1, column=0)
manufacturer_part_number_entry = tk.Entry(root)
manufacturer_part_number_entry.grid(row=1, column=1)

tk.Label(root, text="Footprint:").grid(row=2, column=0)
footprint_entry = tk.Entry(root)
footprint_entry.grid(row=2, column=1)

tk.Label(root, text="Product Package Type:").grid(row=3, column=0)
product_package_type_entry = tk.Entry(root)
product_package_type_entry.grid(row=3, column=1)

tk.Label(root, text="Part PDF Link:").grid(row=4, column=0)
part_pdf_link_entry = tk.Entry(root)
part_pdf_link_entry.grid(row=4, column=1)

tk.Label(root, text="Manufacturer Website:").grid(row=5, column=0)
manufacturer_website_entry = tk.Entry(root)
manufacturer_website_entry.grid(row=5, column=1)

tk.Label(root, text="When do you expect to use it?:").grid(row=6, column=0)
excepted_day_of_usage_entry = tk.Entry(root)
excepted_day_of_usage_entry.grid(row=6, column=1)


def sendEmail():
    manufacturer = manufacturer_entry.get()
    manufacturer_part_number = manufacturer_part_number_entry.get()
    footprint = footprint_entry.get()
    product_package_type = product_package_type_entry.get()
    part_pdf_link = part_pdf_link_entry.get()
    manufacturer_website = manufacturer_website_entry.get()
    expected_day_of_usage = excepted_day_of_usage_entry.get()
    sender = email
    receiver = "rayanciao09@gmail.com"

    subject = "New Part Require"
    body = """"""
    # header

    print(sender)
    print(password)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    body = f"""
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
        messagebox.showinfo("Success", "Part requested successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Unable to log in. Please, make sure your email and password are correct.")
    server.quit()


submit_button = tk.Button(root, text="Submit", command=sendEmail)
submit_button.grid(row=7, columnspan=2)

root.mainloop()

