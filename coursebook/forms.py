from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.fields.html5  import DateField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,Regexp
from flask_login import current_user

# Course information
class SearchByCourseCode(FlaskForm):
    coursecode = StringField("Enter Course Code",
        validators=[DataRequired(),Length(min=5)])
    submit=SubmitField(label='Continue')

#CourseInfo 1
class courseInfo1(FlaskForm):
    coursename = StringField("Course Name",
        validators=[DataRequired(),Length(min=2)])
    studentclass = StringField("Class",
        validators=[DataRequired(),Length(min=2)])

    #changes made
    branch=StringField("Branch",
        validators=[DataRequired(),Length(min=2)])


    semester = StringField("Semester",
        validators=[DataRequired(),Length(min=1)])
    academicyear = StringField("Academic year",
        validators=[DataRequired(),Length(min=5)])

    #changes made
    prepared_by=StringField("Prepared by",
        validators=[DataRequired(),Length(min=3)])

    submit=SubmitField(label='Add Coursebook Information')

# CourseInfo2
class courseInfo2(FlaskForm):
    lects = StringField("Number of Lectures per week",
        validators=[DataRequired(),Length(min=1)])
    tuts = StringField("Number of Tutorials per week",
        validators=[DataRequired(),Length(min=1)])
    practicals = StringField("Number of practicals per week",
        validators=[DataRequired(),Length(min=1)])
    credits = StringField("Credits",
        validators=[DataRequired(),Length(min=1)])
    submit=SubmitField(label='Add Course Information')

# Pre-Requisites
class pre_requisites(FlaskForm):
    pre_reqs = TextAreaField("Enter pre-requisites",
        validators=[DataRequired(),Length(min=3)])
    submit=SubmitField(label='Add Pre-requisites')

# Textbooks
class textbooksForm(FlaskForm):
    txtbooks = TextAreaField("Enter textbooks",
        validators=[DataRequired(),Length(min=5)])
    submit=SubmitField(label='Add Textbooks')

# References
class referencesForm(FlaskForm):
    refs = TextAreaField("Enter references",
        validators=[DataRequired(),Length(min=5)])
    submit=SubmitField(label='Add References')

# Course Objectives
class courseObjectivesForm(FlaskForm):
    crseObjs = TextAreaField("Enter Course Objectives",
        validators=[DataRequired(),Length(min=5)])
    submit=SubmitField(label='Add Course Objectives')

# Course Outcomes
class courseOutcomesForm(FlaskForm):
    #COs and Bloom’s Cognitive level and Descriptor

    co1 = StringField("Course Outcome 1 (CO1)")
    co1level= StringField("Bloom’s Cognitive Level")
    co1Desc= StringField("Bloom’s Cognitive Descriptor")

    co2 = StringField("Course Outcome 2 (CO2)")
    co2level= StringField("Bloom’s Cognitive Level")
    co2Desc= StringField("Bloom’s Cognitive Descriptor")

    co3 = StringField("Course Outcome 3 (CO3)")
    co3level= StringField("Bloom’s Cognitive Level")
    co3Desc= StringField("Bloom’s Cognitive Descriptor")

    co4 = StringField("Course Outcome 4 (CO4)")
    co4level= StringField("Bloom’s Cognitive Level")
    co4Desc= StringField("Bloom’s Cognitive Descriptor")

    submit=SubmitField(label='Add Course Outcomes')

#Course Content
class courseContentsForm(FlaskForm):
    mod1Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod1Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod1Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])
    
    mod2Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod2Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod2Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])

    mod3Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod3Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod3Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])

    mod4Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod4Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod4Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])
    
    mod5Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod5Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod5Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])
    
    mod6Title=StringField("Enter Module Title",
        validators=[DataRequired(),Length(min=2)])
    mod6Hours=StringField("Enter Module Hours",
        validators=[DataRequired(),Length(min=1)])
    mod6Desc=TextAreaField("Enter Module Description",
        validators=[DataRequired(),Length(min=5)])
    submit=SubmitField(label='Add Course Content')