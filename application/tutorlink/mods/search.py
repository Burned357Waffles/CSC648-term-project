# # Handles searching/browsing related pages
# Jeremy W
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor
from tutorlink.db.db import db

# libs
from flask import render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from sqlalchemy import func


# # # Form layouts
class search_form(FlaskForm):
    search_subject = SelectField("Subject")
    search_term = StringField(
        "Search Term"
    )
    search_submit = SubmitField(
        "Search"
    )

# Creates form with dropdown options pre-filled
def new_form():
    form = search_form()

    # Populate subjects to DB
    # Possible TODO, optimize this
    subj = ["All Subjects"]
    for i in Subject.query.all():
        subj.append(i.subj_short)
    form.search_subject.choices = subj
    return form

# Makes form available for navbar to generate
app.jinja_env.globals.update(search_form=new_form)


# # # Routes

# Main search page
# GET -> Empty results page
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


@app.route("/search", methods=['GET'])
def no_results():
    return redirect(url_for("index"))


@app.route("/search/<string:subject>", methods=['GET'])
def subject_search(subject):
    # Get list of tutor
    # TODO optimize?
    # Filter By Subject if needed
    res = Tutor.query.join(Subject)

    # Add subject to query from URL
    res = res.filter(Subject.subj_short == subject)

    # Preform Query
    res = res.all()

    # Render search page with result
    return render_template("search.jinja2", res=res, subj_db=Subject)


# POST -> View results
@app.route("/search", methods=['POST'])
def search_page():
    # Create form
    form = new_form()

    # Form submit | Returns search results
    if form.validate_on_submit():
        # Get list of tutor
        # TODO optimize?
        # Filter By Subject if needed
        res = Tutor.query.join(Subject)

        # Add subject to query if applicable
        if form.search_subject.data != "All Subjects":
            # Get the subject id
            # subj = Subject.query.filter_by(subj_short=form.search_subject.data).first()
            # append subject restriction to query
            res = res.filter( Subject.subj_short==form.search_subject.data)

        # Like search based off of search term if it exists
        if form.search_term.data != "":
            res = res.filter(
                Tutor.tutor_name.like("%" + form.search_term.data + "%") |
                Tutor.tutor_bio.like("%" + form.search_term.data + "%") |
                Tutor.tutor_subj_num.like("%" + form.search_term.data + "%") |
                Subject.subj_short.like("%" + form.search_term.data + "%") |
                Subject.subj_long.like("%" + form.search_term.data + "%")
            )

        # Preform Query
        res = res.all()

        # Render search page with result
        return render_template("search.jinja2", res=res, subj_db=Subject)
