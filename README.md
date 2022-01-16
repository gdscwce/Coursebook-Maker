# Coursebook-Maker

## Table of contents
* [About the project](#about-the-project)
* 

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
- WTForms : [About WTforms](https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/)
- docx-mailmerge : [Read about docx-mailmerge](https://pbpython.com/python-word-template.html)
- HTML,CSS Jinja

## About Code
- \__init__.py 
  Holds general application setup
  
- forms.py\
  Here Forms are defined as classes.
  
- routes.py\
  This file contains all routing code.
  - How to generate forms
    To create forms from classes in forms.py , import that classes in routes.py .
    After creating form, get the data and insert into mongodb collection. Then render html template with the WTForm.
  
- createDoc.py \
  create_DOC() function from this file is used in routes.py to generate coursebook in doc format.\
  This function use template Coursebook_Template to create well structured output.
  It fetch the json data with fields in Coursebook_Template.\ 
  [Learn about how to create MS word template](https://pbpython.com/python-word-template.html)
 
 - template folder
    It contains html templates.\
    layout.html is base template for application.
    
 - static folder
    It contains main.css

## Installation
1. Clone the repo\
  `git clone https://github.com/revati9834/Coursebook-Maker`
2. Enter Directory\
  `cd coursebook`
3. Install all packages\
  `pip install -r requirements.txt`
4. Run webserver\
  `python app.py`


 
