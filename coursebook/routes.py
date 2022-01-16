from flask import Flask,make_response,render_template,url_for,flash,redirect,request,abort,send_file,send_from_directory

# To create forms defined as classes in forms.py , import that classes 
from coursebook.forms import  SearchByCourseCode,courseInfo1,courseInfo2,pre_requisites,textbooksForm,referencesForm,courseObjectivesForm,courseContentsForm,courseOutcomesForm

from coursebook import app, db
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
import secrets,os
from PIL import Image
import pdfkit
from dotenv import load_dotenv
from bson.json_util import dumps,loads
load_dotenv()

from coursebook.createDoc import create_Doc
from pathlib import Path
import json



@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/searchCode",methods=['GET','POST'])
def  SearchCode():
    form = SearchByCourseCode()

    ccode=form.coursecode.data


    if form.validate_on_submit():
        if hasattr(db, ccode):
            db[ccode].drop()
            return redirect(url_for("courseInformation1",coursecode=ccode))
        else:
            return redirect(url_for("courseInformation1",coursecode=ccode))
    
    return render_template("SearchByCode.html",title="Enter coursecode",form=form)


@app.route("/courseInformation1/<coursecode>",methods=['GET','POST'])
def  courseInformation1(coursecode):
    form = courseInfo1()
    ccode=coursecode

    cname=form.coursename.data
    sclass=form.studentclass.data
    branch=form.branch.data
    sem=form.semester.data
    ac_year=form.academicyear.data
    prepared_by=form.prepared_by.data

    #create colection
    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        ccode_collection.drop()
        crse = {'coursename':cname,'coursecode':ccode,'studentclass':sclass,'branch':branch,'semester':sem,'academicyear':ac_year,'prepared_by':prepared_by}
        ccode_collection.insert_one(crse)
        return redirect(url_for("courseInformation2",coursecode=ccode))
    
    return render_template("courseInfo.html",title="Coursebook Information",form=form,ccode=ccode)

@app.route("/courseInformation2/<coursecode>",methods=['GET','POST'])
def  courseInformation2(coursecode):
    form = courseInfo2()
    ccode=coursecode

    lects=form.lects.data
    tuts=form.tuts.data
    practicals=form.practicals.data
    credits=form.credits.data
    
    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "lectures":{"$exists":"true"}}):
            ccode_collection.remove({"lectures":{"$exists":"true"}})
        crse2 = {'lectures':lects,'tutorials':tuts,'practicals':practicals,'credits':credits}
        ccode_collection.insert_one(crse2)
        return redirect(url_for("prerequisites",coursecode=ccode))
    
    return render_template("courseInfo2.html",title="Course Information",form=form,ccode=ccode)


@app.route("/prerequisites/<coursecode>",methods=['GET','POST'])
def  prerequisites(coursecode):
    form = pre_requisites()
    ccode=coursecode

    pre_reqs=form.pre_reqs.data

    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "pre_reqs":{"$exists":"true"}}):
            ccode_collection.remove({"pre_reqs":{"$exists":"true"}})
        preReqs = {'pre_reqs':pre_reqs}
        ccode_collection.insert_one(preReqs)
        return redirect(url_for("textbooks",coursecode=ccode))
    
    return render_template("pre_requisites.html",title="Pre-requisites",form=form,ccode=ccode)

@app.route("/textbooks/<coursecode>",methods=['GET','POST'])
def  textbooks(coursecode):
    form = textbooksForm()
    ccode=coursecode

    txtbooks=form.txtbooks.data

    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "txtbooks":{"$exists":"true"}}):
            ccode_collection.remove({"txtbooks":{"$exists":"true"}})
        tbooks = {'txtbooks':txtbooks}
        ccode_collection.insert_one(tbooks)
        return redirect(url_for("references",coursecode=ccode))
    
    return render_template("textbooks.html",title="Textbooks",form=form,ccode=ccode)

@app.route("/references/<coursecode>",methods=['GET','POST'])
def  references(coursecode):
    form = referencesForm()
    ccode=coursecode

    refs=form.refs.data

    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "refs":{"$exists":"true"}}):
            ccode_collection.remove({"refs":{"$exists":"true"}})
        data = {'refs':refs}
        ccode_collection.insert_one(data)
        return redirect(url_for("courseobjectives",coursecode=ccode))
    
    return render_template("references.html",title="References",form=form,ccode=ccode)

@app.route("/courseobjectives/<coursecode>",methods=['GET','POST'])
def  courseobjectives(coursecode):
    form = courseObjectivesForm()
    ccode=coursecode

    crseObjs=form.crseObjs.data

    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "crseObjs":{"$exists":"true"}}):
            ccode_collection.remove({"crseObjs":{"$exists":"true"}})
        data = {'crseObjs':crseObjs}
        ccode_collection.insert_one(data)
        return redirect(url_for("courseoutcomes",coursecode=ccode))
    
    return render_template("courseObjectives.html",title="Course Objectives",form=form,ccode=ccode)

@app.route("/courseoutcomes/<coursecode>",methods=['GET','POST'])
def  courseoutcomes(coursecode):
    form = courseOutcomesForm()
    ccode=coursecode

    co1=form.co1.data
    co1level=form.co1level.data
    co1Desc=form.co1Desc.data

    co2=form.co2.data
    co2level=form.co2level.data
    co2Desc=form.co2Desc.data

    co3=form.co3.data
    co3level=form.co3level.data
    co3Desc=form.co3Desc.data

    co4=form.co4.data
    co4level=form.co4level.data
    co4Desc=form.co4Desc.data

    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "co1":{"$exists":"true"}}):
            ccode_collection.remove({"co1":{"$exists":"true"}})
        data = {'co1':co1,'co1level':co1level,'co1Desc':co1Desc,
                'co2':co2,'co2level':co2level,'co2Desc':co2Desc,
                'co3':co3,'co3level':co3level,'co3Desc':co3Desc,
                'co4':co4,'co4level':co4level,'co4Desc':co4Desc}
        ccode_collection.insert_one(data)
        return redirect(url_for("courseContents",coursecode=ccode))
    
    return render_template("courseOutcomes.html",title="Course Outcomes",form=form,ccode=ccode)


@app.route("/courseContents/<coursecode>",methods=['GET','POST'])
def  courseContents(coursecode):
    form = courseContentsForm()
    ccode=coursecode

    mod1Title=form.mod1Title.data
    mod1Hours=form.mod1Hours.data
    mod1Desc=form.mod1Desc.data
    
    mod2Title=form.mod2Title.data
    mod2Hours=form.mod2Hours.data
    mod2Desc=form.mod2Desc.data

    mod3Title=form.mod3Title.data
    mod3Hours=form.mod3Hours.data
    mod3Desc=form.mod3Desc.data

    mod4Title=form.mod4Title.data
    mod4Hours=form.mod4Hours.data
    mod4Desc=form.mod4Desc.data

    mod5Title=form.mod5Title.data
    mod5Hours=form.mod5Hours.data
    mod5Desc=form.mod5Desc.data

    mod6Title=form.mod6Title.data
    mod6Hours=form.mod6Hours.data
    mod6Desc=form.mod6Desc.data


    ccode_collection=db[str(ccode)]

    if form.validate_on_submit():
        if ccode_collection.find({ "mod1Title":{"$exists":"true"}}):
            ccode_collection.remove({"mod1Title":{"$exists":"true"}})
        data = {
            'mod1Title':mod1Title,'mod1Hours':mod1Hours,'mod1Desc':mod1Desc,
            'mod2Title':mod2Title,'mod2Hours':mod2Hours,'mod2Desc':mod2Desc,
            'mod3Title':mod3Title,'mod3Hours':mod3Hours,'mod3Desc':mod3Desc,
            'mod4Title':mod4Title,'mod4Hours':mod4Hours,'mod4Desc':mod4Desc,
            'mod5Title':mod5Title,'mod5Hours':mod5Hours,'mod5Desc':mod5Desc,
            'mod6Title':mod6Title,'mod6Hours':mod6Hours,'mod6Desc':mod6Desc
            }
        ccode_collection.insert_one(data)
        return redirect(url_for("Generate_Coursebook",coursecode=ccode))
    
    return render_template("courseContents.html",title="Course Contents",form=form,ccode=ccode)

@app.route("/Generate_Coursebook/<coursecode>")
def  Generate_Coursebook(coursecode):
    json_data=db[coursecode].find()
    cc=create_Doc(json_data)

    info=db[coursecode].find( {"coursename" :{'$exists':True}})
    course=db[coursecode].find( {"lectures" :{'$exists':True}})
    pre_reqs=db[coursecode].find( {"pre_reqs" :{'$exists':True}})
    txtbooks=db[coursecode].find( {"txtbooks" :{'$exists':True}})
    refs=db[coursecode].find( {"refs" :{'$exists':True}})
    crseObjs=db[coursecode].find( {"crseObjs" :{'$exists':True}})
    crseOutcomes=db[coursecode].find( {"co1" :{'$exists':True}})
    crseContent=db[coursecode].find( {"mod1Title" :{'$exists':True}})

    return render_template("Generate_Coursebook.html",title="Generate coursebook",ccode=coursecode,json_data=info,course=course,pre_reqs=pre_reqs,txtbooks=txtbooks,refs=refs,crseObjs=crseObjs,crseOutcomes=crseOutcomes,crseContent=crseContent)

@app.route("/Generate_Coursebook_doc/<coursecode>")
def  Generate_Coursebook_doc(coursecode):
    return send_file("coursebook - {}.docx".format(
             coursecode),as_attachment=True)
