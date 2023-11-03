import os
from tutorlink import app
from tutorlink.db.models import Subject, Tutor

from flask import render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField


# Define the FileUploadForm with a file field and a submit button
class FileUploadForm(FlaskForm):
    file = FileField("File", validators=[FileRequired()])
    submit = SubmitField("Upload")


@app.route("/fileupload", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        # Get the user ID
        user_id = "1"

        # Check if the "static/users" directory exists, and create it if not
        user_folder = os.path.join("static", "users", user_id)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        # Save the uploaded file with its original filename
        uploaded_file = request.files["file"]
        if uploaded_file:
            # Use the original filename provided by the user
            filename = secure_filename(uploaded_file.filename)
            print(f"Uploaded filename: {filename}")
            file_path = os.path.join(user_folder, filename)
            print(f"File path: {file_path}")
            uploaded_file.save(file_path)

            # Redirect to a success page or do any necessary processing
            return "File uploaded successfully."

    # Render the file upload form
    form = FileUploadForm()
    return render_template("upload.jinja2", form=form)
