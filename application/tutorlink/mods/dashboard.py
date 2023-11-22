from tutorlink import app
from tutorlink.db.models import Subject, Tutor

# libs
from flask import render_template


# # # Routes
@app.route("/dashboard", methods=['GET'])
def dashboard():
    # TODO: change my_posts, sent, and received to be the correct data
    return render_template('dashboard.jinja2', my_posts=Tutor.query.all(), sent=Tutor.query.all(),
                           received=Tutor.query.all(), subj_db=Subject)
