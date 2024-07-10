"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
# from forms import LoginForm
# from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

app.app_context().push()


# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """View homepage"""


    return render_template('homepage.html')

@app.route("/movies")
def all_movies():
    """View all movies"""
    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


    """MY ATTEMPT"""

@app.route("/users")
def all_users():
    """View all users"""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/user/<user_id>")
def show_user(user_id):
    """Show details on particular user"""
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")




    @app.route("/login", methods=['GET', "POST"])
    def login():

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
                
        return render_template("/")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         # Retrieve user data from the database
#         # Your database query code goes here

#         # Check if username exists and password is correct
#         if user and check_password_hash(user.password, password):
#             session["user_id"] = user.id
#             return redirect("/")
#         else:
#             return render_template("login.html", message="Invalid username or password.")

#     return render_template("login.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Submission of user"""
#     form = LoginForm(request.form)

#     user = crud.get_user_by_login(password)

#     if form.validate_on_submit():
#         #Form has been submitted with valid data
#         username = form.username.data
#         password = form.password.data

#         #Check to see if a registered user exists with this username
#         user = users.get_by_username(username)

#         if not user or user['password'] != password:
#             flash("Invalid username or password")
#             return redirect("/login")

#         #Store username in session to keep track of logged in user
#         session["username"] = user['username']
#         flash("Logged in!")
#         return redirect("/movies")

# #Form has not been submitted or data was not valid
#     return render_template("homepage.html", form=form)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
