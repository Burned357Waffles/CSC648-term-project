from flask import Flask, redirect, url_for
from tutorlink.db.db import db
from sys import argv
from flask_login import LoginManager, login_required

app = Flask(__name__)
login_mgr = LoginManager()


# # # ==== Flask Config ==== # # #
app.config["NAME"] = "Team 02's TutorLink"
app.config["VERSION"] = "a0.0.1"
app.secret_key = 'wF8gDjUWUf$&&^K'


# # # ==== DB Config ==== # # #
# Setup Local SQLite session in mem for testing
if app.debug:
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Connect to ProdDB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:L244VJw6xGoE19UR@localhost/prod'



# # # ==== Sub modules === # # #
# Imports modules with additional routes
# About Page
import tutorlink.mods.about
# Search Page
import tutorlink.mods.search
# User Account Pages
import tutorlink.mods.account
# Tutor Profile Pages
import tutorlink.mods.tutor


# # DB init
with app.app_context():
    db.init_app(app)
    db.create_all()


# # # ==== Index ==== # # #
# Should be only route in __init__.py
# Should only ever be a redirect
@app.route("/")
def index():
    return redirect(url_for("search_page"))  # Redirect to the list of students


# Run App
if __name__ == "__main__":
    app.run()




# # # DEBUG - DB POPULATION
# Only runs for for SQLite debug session for local testing
# NOTE : Might create bugs between deployment env and local testing
if app.debug:
    with app.app_context():
        from tutorlink.db.models import Subject, Tutor
        # # Populate subjects manually for testing
        subjs = [
            Subject(
                subj_short="CSC",
                subj_long="Computer Science"
            ),
            Subject(
                subj_short="PHYS",
                subj_long="Physics"
            ),
            Subject(
                subj_short="ENGR",
                subj_long="Engineering"
            )
        ]
        for i in subjs:
            db.session.add(i)
        db.session.commit()
        # # Populate Tutors
        tutors = [
            Tutor(
                tutor_user="fakeuser",
                tutor_name="Daedalus Nullium",
                tutor_bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                tutor_cv="image/test/li.pdf",
                tutor_photo="image/test/def_pfp.jpg",
                tutor_vid="https://youtu.be/dQw4w9WgXcQ?si=tCj8boDIu7EYF342",
                tutor_subj=1,
                tutor_subj_num="420"
            ),
            Tutor(
                tutor_user="fakeuser",
                tutor_name="Shifty Wifty",
                tutor_bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                tutor_cv="image/test/li.pdf",
                tutor_photo="image/test/def_pfp.jpg",
                tutor_vid="https://youtu.be/dQw4w9WgXcQ?si=tCj8boDIu7EYF342",
                tutor_subj=3,
                tutor_subj_num="13"
            ),
            Tutor(
                tutor_user="fakeuser",
                tutor_name="Lyrical Lexigraphy",
                tutor_bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                tutor_cv="image/test/li.pdf",
                tutor_photo="image/test/def_pfp.jpg",
                tutor_vid="https://youtu.be/dQw4w9WgXcQ?si=tCj8boDIu7EYF342",
                tutor_subj=2,
                tutor_subj_num="060406200728"
            ),
            Tutor(
                tutor_user="fakeuser",
                tutor_name="Chad McMann",
                tutor_bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                tutor_cv="image/test/li.pdf",
                tutor_photo="image/test/def_pfp.jpg",
                tutor_vid="https://youtu.be/dQw4w9WgXcQ?si=tCj8boDIu7EYF342",
                tutor_subj=2,
                tutor_subj_num="1234"
            ),
            Tutor(
                tutor_user="fakeuser",
                tutor_name="Lyra Venpyra",
                tutor_bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                tutor_cv="image/test/li.pdf",
                tutor_photo="image/test/def_pfp.jpg",
                tutor_vid="https://youtu.be/dQw4w9WgXcQ?si=tCj8boDIu7EYF342",
                tutor_subj=1,
                tutor_subj_num="4321"
            )
        ]
        for i in tutors:
            db.session.add(i)
        db.session.commit()

# # # END DEBUG