from flask import Flask, redirect, url_for
from tutorlink.db.db import db

app = Flask(__name__)
# CONFIG
app.config["NAME"] = "Team 02's TutorLink"
app.config["VERSION"] = "a0.0.1"
app.debug = True

# # Sub modules
# About Page
import tutorlink.mods.about

# Index
@app.route("/")
def hello_world():
    return redirect(url_for("about_list"))  # Redirect to the list of students


# Run App
if __name__ == "__main__":
    app.run()
