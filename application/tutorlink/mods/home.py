from tutorlink import app
from tutorlink.db.models import Subject, Tutor
from tutorlink.db.db import db

# libs
from flask import render_template, redirect, url_for, request
from sqlalchemy import func


# # # Routes
@app.route("/home", methods=['GET'])
def index():
    # This is for the newly added tutors section. Orders by last added -> first added
    tutor_list = Tutor.query.order_by(Tutor.tutor_id).all()

    # Get the top 5 subjects from tutors
    top_tutors = db.session.query(Tutor.tutor_subj, func.count(Tutor.tutor_subj).label('count')) \
        .group_by(Tutor.tutor_subj) \
        .order_by(func.count(Tutor.tutor_subj).desc()) \
        .limit(5) \
        .all()

    # Make a list of the short subject name
    subject_list = []
    for tutor_subj, _ in top_tutors:
        subject = Subject.query.filter_by(subj_id=tutor_subj).first()
        if subject:
            subject_list.append({"text": subject.subj_short})

    return render_template('home.jinja2', subj_db=Subject, subject_list=subject_list, tutor_list=tutor_list)
