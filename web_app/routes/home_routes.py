from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
def hello():
    print("VISITED THE HELLO PAGE")
    return "Hello World!"

@home_routes.route('/about')
def about():
    print("Visited the about page!")
    return "About Me!"