# # Handles display a tutor profile
# Abel S, Jeremy W, Ankita M
# app
from tutorlink import app
from tutorlink.db.db import db 
from tutorlink.db.models import Subject, Tutor, Tutor_Request

# flask-libs
from flask import redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from flask_login import current_user
# libs
import re
from uuid import uuid4
from os import makedirs, path

class tutor_app_form(FlaskForm):
    name = StringField("Full Name")
    bio = TextAreaField("Bio")
    subjects = SelectField("Subjects", choices=[])
    subject_num = StringField("Subject Number")
    video = StringField("Video Link (YouTube)")
    cv_file = FileField("Upload CV/Flyer (.pdf)")
    pic_file = FileField("Upload Photo (.jpg)")
    submit = SubmitField("Apply")


# Tutor Application Route
@app.route('/tutor/register', methods=['GET', 'POST'])
def tutor_app_page():
    # Load form
    form = tutor_app_form()

    # Populate form with subject data
    subj = []
    for i in Subject.query.all():
        subj.append(i.subj_short)
    form.subjects.choices = subj

    # Apply tutor application
    if form.validate_on_submit():
        # TODO : Store info if not logged in

        # Redirect to login page if not logged in
        if not current_user.is_authenticated:
            return redirect(url_for('login_page'))

        # Assume validation in debug mode
        # Else push to request db
        tutor = None
        if(app.debug):
            tutor = Tutor()
        else:
            tutor = Tutor_Request()

        # Populate tutor app object to be pushed to db
        # Only populates first run data
        tutor.tutor_name = form.name.data
        tutor.tutor_bio = form.bio.data
        if(form.video.data == ""):
            tutor.tutor_vid = None
        else:
            tutor.tutor_vid = form.video.data
        # Special Case for subject
        tutor.tutor_subj = int(Subject.query.filter_by(subj_short=form.subjects.data).first().subj_id)
        tutor.tutor_subj_num = form.subject_num.data

        # Get current user for user value
        if(not current_user.is_authenticated):
            return redirect(url_for('register_page'))
        tutor.tutor_user = current_user.user_id

        # File upload
        static_path = "tutorlink/static/tutors/"
        # Gen UUID for profile folder for file upload
        file_dir = str(uuid4())

        # UUID Collision checking and regen
        # I know its technically unneeded but /shrug
        while(path.exists(static_path + file_dir)):
            file_dir = str(uuid4())

        # Make tutor director
        makedirs(path.join(static_path, file_dir))
        
        # Picture upload
        # No file uploaded case
        if (form.pic_file and form.pic_file.data.filename == '' and not '.jpg' in form.pic_file.data.filename):
            tutor.tutor_photo = None
        # Photo provided
        else:
            tutor.tutor_photo = file_dir
            form.pic_file.data.save(path.join(static_path, file_dir, "photo.jpg"))
        
        # CV/Flyer upload
        # No file uploaded case
        if (form.cv_file and form.cv_file.data.filename == '' and not '.pdf' in form.cv_file.data.filename):
            tutor.tutor_cv = None
        # Photo provided
        else:
            tutor.tutor_cv = file_dir
            form.cv_file.data.save(path.join(static_path, file_dir, "cv.pdf"))

        # Push to DB
        db.session.add(tutor)
        db.session.commit()

        # redirect to tutor page if in debug
        if(app.debug):
            return redirect(url_for('tutor_profile', tutor_id=tutor.tutor_id))   
        return redirect(url_for("index"))  
    
    # Return Registration form
    return render_template('tutor_app_template.jinja2', form=form)


# This is so that users can see the filename of the CV
def file_name_from_cv(tutor_cv):
    return re.search("[^\/]+$", tutor_cv).group(0)

# Makes function available for tutor.jinja2 to call
app.jinja_env.globals.update(cv_filename=file_name_from_cv)

# TODO: add a url parameter for specific tutors
# Test template for for tutor page
@app.route("/tutor/view/<int:tutor_id>", methods=['GET'])
def tutor_profile(tutor_id):
    # Query for tutor to view
    tutor = Tutor.query.filter_by(tutor_id=tutor_id).first()
    # Redirect to index if not found
    if not tutor:
        return redirect(url_for('index'))
    # Display result
    return render_template("tutor.jinja2", tutor=tutor, subj_db=Subject)


