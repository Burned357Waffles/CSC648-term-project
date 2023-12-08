from tutorlink import app
from tutorlink.db.models import Subject, Tutor, Message

# libs
from flask import render_template, redirect, url_for
from flask_login import current_user


# # # Routes
@app.route("/dashboard", methods=['GET'])
def dashboard():
    # Redirect to login page if user not currently signed in
    if not current_user.is_authenticated:
        return redirect(url_for("login_page"))

    my_posts = Tutor.query.filter(Tutor.tutor_user == current_user.user_id).all()

    # TODO: change my_posts, sent, and received to be the correct data
    return render_template('dashboard.jinja2', my_posts=my_posts, sent=Tutor.query.all(),
                           received=Tutor.query.all(), subj_db=Subject)
