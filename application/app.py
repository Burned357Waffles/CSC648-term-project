from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


# CONFIG
app.config["NAME"] = "Team 02's Tutorio"
app.config["VERSION"] = "a0.0.1"
app.debug = True

# # Sub modules
import mods.about

# Index
@app.route("/")
def hello_world():
    return redirect(url_for("about_list"))  # Redirect to the list of students


# Run App
if __name__ == "__main__":
    app.run()

