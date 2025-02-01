# EasyEDA Part Requester
A python script to request parts from EasyEDA

let's assume you need some part for your projetc in EasyEDA, but the part is not available from their library, using this app you can 

## Installation
1. Download the latest release from the [Releases](https://github.com/Rayanlupo/EasyEDA-Part-Requester) page.
2. open `.env`
2. Replace `your_email@example.com` and `your_password` with your actual email and password.
3. Save the file.. 
4. Run `app.exe` or `script.exe`.

## Build from Source
### 1. Prerequisites
- Python 3.11 or later
- pip (Python package installer)
- virtualenv (recommended)
- Pyinstaller, use the following command if you don't already have it:
```bash
pip install pyinstaller
```
And now you should be ready to continue
###2. Clone the repository
Clone the repository from github
```bash
git clone https://github.com/your-username/easyeda-part-requester.git
cd easyeda-part-requester
```

### 3. Install dependencies:
Set up the virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Install the required Python packages
```bash
pip install -r requirements.txt
```
### 4. Setup the environment variabelsù
Edit the .env file to add your email and your password
#### If your account has 2FA on 
you have to generate an app password from the your google account settings:
1. Go to Setting -> Security -> 2-Step Verification -> App Passwords
2. Insert the name you prefer and click "Generate", it will show the password only once so make sure to copy and paste it into the .cfg file in your documents folder before closing the window or generate a new config file by just running the application for the first time and by filling up the form that'll pop up.
```plaintext
EMAIL=your_email@example.com
PASSWORD=your_password
```
### 5.  Build the executable
Use pyinstaller to create the executable file
- if you prefer to open the terminal window
```bash
pyinstaller --onefile --console script.py
```
- if you want to open a classic popup window:
```bash
pyinstaller --onefile --windowed app.py
```

###6. Run the executable file
- On Windows: Double-click on the executable file in the file explorer
-On Linux/Mac: Run in the terminal:
```bash
./dist/app
```
or

```bash
./dist/script
```
## Licence
EasyEDA Part Requester © 2025 by Guebre Nadir Rayane is licensed under CC BY-NC 4.0. For more infos please visit: https://creativecommons.org/licenses/by-nc/4.0/

## Issues

For any issue, please:
- Open an issue through the Github Repository
- Contact me through my socials or email, available on my Github profile.
