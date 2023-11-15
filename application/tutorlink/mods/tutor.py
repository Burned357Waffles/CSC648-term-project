# # Handles display a tutor profile
# Abel S
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
# Test template for for tutor page
@app.route("/tutor/view/<int:tutor_id>", methods=['GET'])
def tutor_profile(tutor_id):
    # TODO : Query specific tutor for db
    tutor = Tutor.query.first()

    return render_template("tutor.jinja2", tutor=tutor, subj_db=Subject)