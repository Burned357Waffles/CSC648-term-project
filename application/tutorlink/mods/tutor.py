# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template
import re


# This is so that users can see the filename of the CV
def file_name_from_cv(tutor_cv):
    return re.search("[^\/]+$", tutor_cv).group(0)

# Makes function available for tutor.jinja2 to call
app.jinja_env.globals.update(cv_filename=file_name_from_cv)


# TODO: add a url parameter for specific tutors
@app.route("/tutor", methods=['GET'])
def tutor_profile():
    # TODO: better DB query so we get specific tutor + have their subject already joined with them
    tutor = (Tutor.query.all())[2]

    return render_template("tutor.jinja2", tutor=tutor, subj_db=Subject)