#import mysql.connector  #then write mysql.connector.connect
import mysql.connector as mysql # then write mysql.connect
import json
from flask import make_response

class user_model():
    def __init__(self):
        try:
            #Connection establishment code.
            #connection = mysql.connect(host="localhost", user="root", port='3306', password="12345", database="flask_demo")
            #con=mysql.connecter.connect(user="root", password="12345", host="localhost", database="flask_demo")
            self.con=mysql.connect(user="root", password="12345", host="localhost", database="flask_demo")
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary = True)
            print("connection successful")
        except mysql.error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else: 
                print(err)
        else:
            print("some error")
    def user_signup_model(self, name):
        #business logic
        #Query execution code. 
        self.cur.execute("SELECT * FROM users")
        result= self.cur.fetchall()
        print(result)
        if len(result) > 0:
            temp = make_response({"payload":result}, 200) #json.dumps(result)
            temp.headers ['Access-Control-Allow-Origin'] = "*"
            return temp
        else:
            temp = make_response({"message":"No Data Found"}, 204)
            temp.headers ['Access-Control-Allow-Origin'] = "*"
            return temp

    def user_getall_model(self, name):
        #business logic
        #Query execution code. 
        self.cur.execute("SELECT * FROM users")
        result= self.cur.fetchall()
        print(result)
        if len(result) > 0:
            temp = make_response({"payload":result}, 200) #json.dumps(result)
            temp.headers ['Access-Control-Allow-Origin'] = "*"
            return temp
        else:
            temp = make_response({"message":"No Data Found"}, 204)
            temp.headers ['Access-Control-Allow-Origin'] = "*"
            return temp
        
    def user_addone_model(self, userdata):
        #business logic
        #Query execution code.
        #print(userdata['email_id']); 
        self.cur.execute(f"INSERT INTO users(username, email_id, phone_no, password) VALUES ('{userdata['username']}', '{userdata['email_id']}', '{userdata['phone_no']}', '{userdata['password']}')")
        return make_response({"message":"User created Successfully"}, 200)
    
    def user_update_model(self, userdata):
        #business logic
        #Query execution code.
        print(f"UPDATE users SET username= '{userdata['username']}', email_id= '{userdata['email_id']}', phone_no= '{userdata['phone_no']}', password= '{userdata['password']}' WHERE id= {userdata['id']}")
        self.cur.execute(f"UPDATE users SET username= '{userdata['username']}', email_id= '{userdata['email_id']}', phone_no= '{userdata['phone_no']}', password= '{userdata['password']}' WHERE id= {userdata['id']}")
        print(userdata['id']);
        if self.cur.rowcount>0:
            return make_response({"message":"User data update successfully"}, 200)
        else:
            return make_response({"message":"nothing to update"}, 202)
        
    def user_delete_model(self, userdata):
        #business logic
        #Query execution code.
        print(userdata);
        if type(userdata) is str:
            print("This line will be executed", type(userdata))
            self.cur.execute(f"DELETE FROM users WHERE id= {userdata}")
            print(userdata);
            if self.cur.rowcount>0:
                return make_response({"message":"User data deleted successfully"}, 200)
            else:
                return make_response({"message":"Nothing to delete"}, 202)
        else:
            print("Not an integer", type(userdata))
            self.cur.execute(f"DELETE FROM users WHERE id= {userdata['id']}")
            print(userdata['id']);
            if self.cur.rowcount>0:
                return make_response({"message":"User data deleted successfully"}, 200)
            else:
                return make_response({"message":"Nothing to delete"}, 202)
    
    def user_patch_model(self, userdata, id):
        #"UPDATE users SET username= '{userdata['username']}', email_id= '{userdata['email_id']}', phone_no= '{userdata['phone_no']}', password= '{userdata['password']}' WHERE id= {userdata['id']}"
        qry = f"UPDATE users SET "
        for key in userdata:
            if key != "id":
                qry += f" {key} = '{userdata[key]}',"
        qry = qry[:-1] + f" WHERE id = {id}"
        #qry += f"WHERE id = {userdata['id']}"
        self.cur.execute(qry)
        #return qry
        if self.cur.rowcount>0:
            return make_response({"message":"User data update successfully"}, 200)
        else:
            return make_response({"message":"nothing to update"}, 202)
         
    def user_pagination_model(self, limit, page):
       #return "Page model"
       limit= int(limit)
       page = int(page)
       start = (page * limit) - limit
       qry = f"SELECT * FROM users LIMIT {start}, {limit}"
       self.cur.execute(qry)
       result = self.cur.fetchall()
       print(limit, page, "Page model", result)
       if len(result) > 0 :
            res = make_response({"payload" : result, "page_no" : page, "limit_no" : limit}, 200)
            return res
       else:
            return make_response({"message": "No data found"}, 204)  
    
    def user_upload_avatar_model(self, uid, img_filepath):
        #return f"UPDATE users SET user_pic = '{img_filepath}' WHERE id= {uid}"
        self.cur.execute(f"UPDATE users SET user_pic = '{img_filepath}' WHERE id= '{uid}'")
        if self.cur.rowcount>0:
            return make_response({"message":"User profile pic uploaded successfully", "user_pic" : img_filepath}, 200)
        else:
            return make_response({"message":"nothing to uplod"}, 202)