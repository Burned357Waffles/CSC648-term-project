from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# CONFIG
app.config["NAME"] = "Team 02's Tutorio"
app.config["VERSION"] = "a0.0.1"

# Dictionary to store information about 6 people
people_info = {
    "person1": {
        "name": "Person 1",
        "bio": "This is the bio of Person 1.",
    },
    "person2": {
        "name": "Person 2",
        "bio": "This is the bio of Person 2.",
    },
    "person3": {
        "name": "Person 3",
        "bio": "This is the bio of Person 3.",
    },
    "person4": {
        "name": "Person 4",
        "bio": "This is the bio of Person 4.",
    },
    "person5": {
        "name": "Person 5",
        "bio": "This is the bio of Person 5.",
    },
    "person6": {
        "name": "Person 6",
        "bio": "This is the bio of Person 6.",
    },
}


# Index
@app.route("/")
def hello_world():
    return redirect(url_for("about_list"))  # Redirect to the list of people


# About me index (list of people)
@app.route("/about")
def about_list():
    return render_template("about_list.html")  # Render the list of people template


# Load template for individual about me pages
@app.route("/about/<string:person>")
def about_page(person):
    if person in people_info:
        return render_template("about_template.html", person=people_info[person])
    else:
        return "Person not found"


# Run App
if __name__ == "__main__":
    app.run()
