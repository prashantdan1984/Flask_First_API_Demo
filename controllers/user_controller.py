from app import app
from model.user_model import user_model
from flask import request
obj = user_model()

@app.route("/user/signup")
def signup():
    #return "Welcome to signup screen1"
    return obj.user_signup_model("danbapu");

@app.route("/user/getall")
def user_getall_controller():
    #return "Welcome to signup screen1"
    return obj.user_getall_model("get all model");

@app.route("/user/addone", methods = ['POST'])
def user_addone_controller():
    print(request.form)
    #return "Welcome to signup screen1"
    return obj.user_addone_model(request.form);

@app.route("/user/update", methods = ['PUT'])
def user_update_controller():
    print(request.form)
    #return "Welcome to signup screen1"
    return obj.user_update_model(request.form);

@app.route("/user/delete", methods = ['DELETE'])
def user_delete_controller():
    print(request.form)
    #return "Welcome to signup screen1"
    return obj.user_delete_model(request.form);

@app.route("/user/delete1/<id>", methods = ['DELETE'])
def user_delete1_controller(id):
    #return "Welcome to signup screen1"
    return obj.user_delete_model(id);