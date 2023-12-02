# # Handles display a tutor profile
# app
from tutorlink import app
from tutorlink.db.models import Subject, Tutor, Message, User

# libs
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators


# # # Form layouts
# Messaging form created now so actual BE integration later will be less painful
class message_form(FlaskForm):
    message_body = TextAreaField(
        "Message Body",
        validators=[validators.length(max=512)],  # so that the message field is limited on user-side
        render_kw={"placeholder": "Please include your contact info so that the tutor can get back to you . . .",
                   "autofocus": "true"}
    )
    message_submit = SubmitField(
        "Send"
    )

# Makes form available for send_message.jinja2 to generate
app.jinja_env.globals.update(message_form=message_form)


# TODO: add a url parameter for specific tutors
# Test template for messaging page
@app.route("/message/tutor/<int:tutor_id>", methods=['GET', 'POST'])
def message_tutor(tutor_id):
    tutor = Tutor.query.filter(Tutor.tutor_id == tutor_id).first()

    if request.method == 'GET':
        return render_template("send_message.jinja2", tutor=tutor, subj_db=Subject)

    # TODO: Redirect user to Dashboard with flash message showing success state of message sending
    if request.method == 'POST':
        return redirect(url_for("index"))

# Allows a user to view the messages they have sent or received
@app.route("/message/view/<int:msg_id>", methods=['GET'])
def view_message(msg_id):
    # TODO: check if the user is allowed to access the specified message
    message = Message.query.first()

    student_user_id = message.msg_student
    student_user = User.query.filter(User.user_id == student_user_id).first()

    # tutor_user_id = message.msg_tutor
    # tutor_user = User.query.filter(User.user_id == tutor_user_id).first()

    tutor_listing = message.msg_listing
    tutor = Tutor.query.filter(Tutor.tutor_id == tutor_listing).first()

    subject = Subject.query.filter_by(subj_id=tutor.tutor_subj).first().subj_short + ' ' + tutor.tutor_subj_num

    # TODO: check if user is the sender or the receiver
    return render_template("view_message.jinja2", student=student_user, tutor=tutor,
                           subject=subject, message=message.msg_text)

