from flask import Flask

app = Flask(__name__)

#import controllers.user_controller as user_controller
#from controllers import user_controller, product_controller
from controllers import *

@app.route("/")
def welcome():
    return "Hello Word prashantkumar"

@app.route("/home")
def home():
    return "Welcome to home danbapu"

#import user_controller

