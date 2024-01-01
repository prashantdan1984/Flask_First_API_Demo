from app import app
from model.user_model import user_model
from flask import request, send_file
from datetime import datetime
obj = user_model()

@app.route("/user/signup")
def signup():
    return obj.user_signup_model("danbapu");

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model("get all model");

@app.route("/user/addone", methods = ['POST'])
def user_addone_controller():
    print(request.form)
    return obj.user_addone_model(request.form);

@app.route("/user/update", methods = ['PUT'])
def user_update_controller():
    print(request.form)
    return obj.user_update_model(request.form);

@app.route("/user/delete", methods = ['DELETE'])
def user_delete_controller():
    print(request.form)
    return obj.user_delete_model(request.form);

@app.route("/user/delete1/<id>", methods = ['DELETE'])
def user_delete1_controller(id):
    return obj.user_delete_model(id);

@app.route("/user/patch/<id>", methods = ['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id);

@app.route("/user/getall/limit/<limit>/page/<page>", methods = ['GET'])
def user_pagination_controller(limit, page):
    print("page controller")
    return obj.user_pagination_model(limit, page)

@app.route("/user/<uid>/upload/avatar", methods = ['PUT'])
def user_upload_avatar_controller(uid):
    timestamp = str(datetime.now().timestamp()).replace(".", "_")
    imgfile = request.files["avatar"]
    img_filepath = f"user_profile_pics/{uid}_{timestamp}_{imgfile.filename}"
    imgfile.save(img_filepath)
    print(imgfile)
    return  obj.user_upload_avatar_model(uid, img_filepath)

@app.route("/user_profile_pics/<filename>")
def user_getprofile_controller(filename):
    return send_file(f"user_profile_pics/{filename}")