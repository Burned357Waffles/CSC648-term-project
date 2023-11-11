# # Handles account management related functions
# Jeremy W
from tutorlink import app
from tutorlink.db.models import User
from tutorlink.db.db import db

# libs
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# # Account Registration Page
class register_form(FlaskForm):
    username = StringField("Username")
    password = StringField("Password")
    email = StringField("Email")
    submit = SubmitField("Create Account")

@app.route("/acc/register", methods=['POST','GET'])
def register_page():
    # Create form for user reg
    form = register_form()

    # Validate account creation
    # Push to db on success
    # Return error on failure
    if form.validate_on_submit():
        # Verify empty fields
        if form.email.data == "" or form.password.data == "" or form.username.data == "":
            return "Error : Empty Field"

        # Verify SFSU Email
        if not "@sfsu.edu" in form.email.data:
            return "Error : Creating an account requires SFSU Email"
        
        # Verify PW requirements
        # TODO : This

        # Verify account doesn't already exist
        existing_user = User.query.filter_by(user_name=form.username.data).all()
        if len(existing_user) != 0:
            return("Error: User already exists")
        
        # Verify email isn't already used
        existing_user = User.query.filter_by(user_email=form.email.data).all()
        if len(existing_user) != 0:
            return("Error: Email already in use")

        # Create new user account object
        new_acc = User(
            user_name=form.username.data,
            user_pw=form.password.data,
            user_email=form.email.data
        )

        # Push new user account to db
        db.session.add(new_acc)
        db.session.commit()

        # Redirect to login page for user loggin
        # Possible TODO autologin and redirect to home page

        # Return to index for redirect to home page
        return redirect(url_for("index"))


    # Return for for user creation
    return render_template("default_form.jinja2", form=form)



# # Account Login page
@app.route("/acc/login", methods=['POST','GET'])
def login_page():
    return "login page"

# # Debug Routes
if app.debug:
    @app.route("/acc/debug")
    def acc_debug():
        res = User.query.all()
        ret = ""
        for i in res:
            ret = ret + i.usr2str()
        return(ret)


