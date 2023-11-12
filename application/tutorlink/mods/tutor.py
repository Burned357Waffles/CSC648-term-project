# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template

@app.route("/tutor", methods=['GET'])
def tutor_profile():
    tutor = Tutor.query.first()
    
    print(tutor)
    print(tutor.tutor_name)
    print(tutor.tutor_bio)
    print(tutor.tutor_cv)
    print(tutor.tutor_photo)
    print(tutor.tutor_vid)
    print(tutor.tutor_subj)
    print(tutor.tutor_subj_num)

    return render_template("tutor.jinja2", res=None)