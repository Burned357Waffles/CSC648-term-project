# # Handles searching/browsing related pages
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

# # # Form layouts
class search_form(FlaskForm):
    search_subject = SelectField("Subject")
    search_term = StringField(
        "Search Term"
    )
    search_submit = SubmitField(
        "Search"
    )

def new_form():
    form = search_form()

    # Populate subjects to DB
    # Possible TODO, optimize this
    subj = ["All Subjects"]
    for i in Subject.query.all():
        subj.append(i.subj_short)
    form.search_subject.choices = subj

    return form

app.jinja_env.globals.update(search_form=new_form)


# # # Routes
# Sample home page
@app.route("/test", methods=['GET'])
def home_page():
    return render_template("test.jinja2", res=None)

# Main search page
# POST -> View results
@app.route("/test", methods=['POST'])
def search_test():
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
            res = res.filter(Subject.subj_short == form.search_subject.data)

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
        return render_template("test.jinja2", res=res, subj_db=Subject)
