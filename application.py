from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_session import Session
from flask import Flask, session, render_template
from wtform_fields import *
import os
import requests

# Configure app
app = Flask(__name__)
app.secret_key = 'replace'
os.environ["DATABASE_URL"] = "postgres://ukbwquwkkrusjs:f7b77b830c7bc72df39a6c200b69bda32a0f381b225508a849b842784e230157@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d9jpnfbvjl7tkt"


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET', 'POST'])
def index():
    # res = requests.get("https://www.goodreads.com/book/review_counts.json",
    #                    params={"key": "lRj6fWPLwTIg0B84ShylA", "isbns": "9781632168146"})
    # print(res.json())
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return "Great Success"

    return render_template("index.html", form = reg_form)


if __name__ == "__main__":
    app.run(debug=True)
