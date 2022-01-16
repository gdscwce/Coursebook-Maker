import json
from pathlib import Path
import os

from mailmerge import MailMerge

def create_Doc(coursebook_json):
    script_location=Path("coursebook")
    file_location=script_location

    template=file_location/"Coursebook_Template.docx"
    document= MailMerge(template)

    for coursebook in coursebook_json:
        if coursebook.get('coursename'):
            coursecode=coursebook["coursecode"]
            document.merge(
                Coursename=coursebook["coursename"],
                Coursecode=coursebook["coursecode"],
                Year_first_year=coursebook["studentclass"],
                Branch=coursebook["branch"],
                Semester=coursebook["semester"],
                Academic_year=coursebook["academicyear"],
                Prepared_by=coursebook["prepared_by"]
                )
        if coursebook.get('lectures'):
            document.merge(
                Lects=coursebook["lectures"],
                Tuts=coursebook["tutorials"],
                Practicals=coursebook["practicals"],
                Credits=coursebook["credits"]
                )
        if coursebook.get('pre_reqs'):
            document.merge(
                pre_requisites=coursebook["pre_reqs"]
                )
        if coursebook.get('txtbooks'):
            document.merge(
                Textbooks=coursebook["txtbooks"]
                )
        if coursebook.get('refs'):
            document.merge(
                References=coursebook["refs"]
                )
        if coursebook.get('crseObjs'):
            document.merge(
                CourseObjectives=coursebook["crseObjs"]
                )
        if coursebook.get('co1'):
            document.merge(
                CO1=coursebook["co1"],
                CO1level=coursebook["co1level"],
                CO1Desc=coursebook["co1Desc"],

                CO2=coursebook["co2"],
                CO2level=coursebook["co2level"],
                CO2Desc=coursebook["co2Desc"],

                CO3=coursebook["co3"],
                CO3level=coursebook["co3level"],
                CO3Desc=coursebook["co3Desc"],

                CO4=coursebook["co4"],
                CO4level=coursebook["co4level"],
                CO4Desc=coursebook["co4Desc"]

                )
        
        if coursebook.get('mod1Title'):
            document.merge(
                Mod1_title=coursebook["mod1Title"],
                Mod1_hours=coursebook["mod1Hours"],
                Mod1_desc=coursebook["mod1Desc"],

                Mod2_title=coursebook["mod2Title"],
                Mod2_hours=coursebook["mod2Hours"],
                Mod2_desc=coursebook["mod2Desc"],

                Mod3_title=coursebook["mod3Title"],
                Mod3_hours=coursebook["mod3Hours"],
                Mod3_desc=coursebook["mod3Desc"],

                Mod4_title=coursebook["mod4Title"],
                Mod4_hours=coursebook["mod4Hours"],
                Mod4_desc=coursebook["mod4Desc"],

                Mod5_title=coursebook["mod5Title"],
                Mod5_hours=coursebook["mod5Hours"],
                Mod5_desc=coursebook["mod5Desc"],

                Mod6_title=coursebook["mod6Title"],
                Mod6_hours=coursebook["mod6Hours"],
                Mod6_desc=coursebook["mod6Desc"],
                )
        
            
        
    #if file exist with same name delete it
    if os.path.exists(file_location/"coursebook - {}.docx".format(
            coursecode,
        )):
        os.remove(file_location/"coursebook - {}.docx".format(
            coursecode,
        ))
    
    doc_copy=document.write(
        file_location/"coursebook - {}.docx".format(
            coursecode,
        )
    )

    return coursecode