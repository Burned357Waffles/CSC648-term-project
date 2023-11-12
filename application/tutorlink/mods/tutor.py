# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template


# TODO: add a url parameter for specific tutors
@app.route("/tutor", methods=['GET'])
def tutor_profile():
    # TODO: better DB query so we get specific tutor + have their subject already joined with them
    tutor = Tutor.query.first()

    return render_template("tutor.jinja2", tutor=tutor, subj_db=Subject)