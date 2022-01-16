# Coursebook-Maker

## About The Project
Coursebook Maker which allows user to build coursebook for any course with details like coursebook information, course information,pre-requisites, textbooks, references, course objectives, course content,etc.User just have to fill up forms that specifies required data.The Data provided by user is stored and fetched with fields in coursebook template. At the end, system automatically generates well structured coursebook. Users have option to download and save the generated coursebook.
  
- Build coursebook with this application.
- Run the app.py and go to localhost:5000
- Add coursebook data
- At the end, View added data and download the coursebook

## Technologies Used
- Python
- Flask (web framework)
- PyMongo (MongoDB driver)
- docx-mailmerge : [Read about docx-mailmerge](https://pbpython.com/python-word-template.html)
- HTML,CSS Jinja

## About Code

## Installation
Clone the repo
'git clone https://github.com/DiptoChakrabarty/Resume-Generator'
Enter Directory
`cd `cd Resume-Generator
Install all packages
pip install -r requirements.txt
Remove site.db file to start fresh database
rm resume/site.db
Setup Env Variables
create file .env inside folder resume

Add the following

MAIL_USERNAME="{{ your gmail username }}"
PASSWORD="{{ your password }}"
Run webserver
python3 app.py


 
