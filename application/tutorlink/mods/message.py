# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


# # # Form layouts
# Messaging form created now so actual BE integration later will be less painful
class message_form(FlaskForm):
    message_body = StringField(
        "Message Body"
    )
    message_submit = SubmitField(
        "Send"
    )

# Makes form available for message.jinja2 to generate
app.jinja_env.globals.update(message_form=message_form)


# TODO: add a url parameter for specific tutors
# Test template for messaging page
@app.route("/message/<int:tutor_id>", methods=['GET', 'POST'])
def message_tutor(tutor_id):
    # TODO : Query specific tutor for db
    tutor = Tutor.query.first()

    if request.method == 'GET':
        return render_template("message.jinja2", tutor=tutor, subj_db=Subject)

    # TODO: Redirect user to Dashboard with flash message showing success state of message sending
    if request.method == 'POST':
        return redirect(url_for("index"))