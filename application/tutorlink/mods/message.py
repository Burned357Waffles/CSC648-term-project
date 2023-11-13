# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template


# TODO: add a url parameter for specific tutors
# Test template for messaging page
@app.route("/message/<int:tutor_id>", methods=['GET'])
def message_tutor(tutor_id):
    # TODO : Query specific tutor for db
    tutor = Tutor.query.first()

    return render_template("tutor.jinja2", tutor=tutor, subj_db=Subject)
