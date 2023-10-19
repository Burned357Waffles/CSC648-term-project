# # Handles searching/browsing related pages

# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor
from tutorlink.db.db import db

# libs
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

# # # Form layouts
class search_form(FlaskForm):
    search_term = StringField(
        "Search Term"
    )
    search_subject = SelectField("Subject")
    search_submit = SubmitField(
        "Search"
    )

# # # Routes

# Main search page
# GET -> Search form
# POST -> View results
@app.route("/search", methods=['POST','GET'])
def search_page():
    # Create form
    form = search_form()

    # Populate subjects to DB
    # Possible TODO, optimize this
    subj = ["Subject"]
    for i in Subject.query.all():
        subj.append(i.subj_short)
    form.search_subject.choices = subj

    # Form submit | Returns search results
    if form.validate_on_submit():
        # Get list of tutor
        # TODO optimize?
        # Filter By Subject if needed
        res = Tutor.query

        # Add subject to query if applicable
        if form.search_subject.data != "Subject":
            # Get the subject id
            subj = Subject.query.filter_by(subj_short=form.search_subject.data).first()
            # append subject restriction to query
            res = res.filter_by( tutor_subj=subj.subj_id)

        # Like search based off of search term if it exists
        if form.search_term.data != "":
            res = res.filter(
                Tutor.tutor_name.like("%" + form.search_term.data + "%") |
                Tutor.tutor_bio.like("%" + form.search_term.data + "%") |
                Tutor.tutor_subj_num.like("%" + form.search_term.data + "%")
            )

        res = res.all()

        # TODO Optimize
        for i in range(0, len(res)):
            res[i].tutor_subj =  Subject.query.filter_by(subj_id=res[i].tutor_subj).first().subj_short

        return render_template("search.jinja2", form=form, res=res)

    return render_template("search.jinja2", form=form, res=None)



