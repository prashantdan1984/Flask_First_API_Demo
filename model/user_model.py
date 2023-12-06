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
            return temp
        else:
            return make_response({"message":"No Data Found"}, 204)

    def user_getall_model(self, name):
        #business logic
        #Query execution code. 
        self.cur.execute("SELECT * FROM users")
        result= self.cur.fetchall()
        print(result)
        if len(result) > 0:
            temp = make_response({"payload":result}, 200) #json.dumps(result)
            return temp
        else:
            return make_response({"message":"No Data Found"}, 204)
        
    def user_addone_model(self, userdata):
        #business logic
        #Query execution code.
        #print(userdata['email_id']); 
        self.cur.execute(f"INSERT INTO users(username, email_id, phone_no, password) VALUES ('{userdata['username']}', '{userdata['email_id']}', '{userdata['phone_no']}', '{userdata['password']}')")
        return make_response({"message":"This is user addone model"}, 201)
    
    def user_update_model(self, userdata):
        #business logic
        #Query execution code.
        self.cur.execute(f"UPDATE users SET username= '{userdata['username']}', email_id= '{userdata['email_id']}', phone_no= '{userdata['phone_no']}', password= '{userdata['password']}' WHERE id= {userdata['id']}")
        print(userdata['id']);
        if self.cur.rowcount>0:
            return make_response({"message":"User data update successfully"}, 201)
        else:
            return make_response({"message":"nothing to update"}, 204)
        
    def user_delete_model(self, userdata):
        #business logic
        #Query execution code.
        print(userdata);
        if type(userdata) is str:
            print("This line will be executed", type(userdata))
            self.cur.execute(f"DELETE FROM users WHERE id= {userdata}")
            print(userdata);
            if self.cur.rowcount>0:
                return make_response({"message":"User data deleted successfully"}, 201)
            else:
                return make_response({"message":"Nothing to delete"}, 204)
        else:
            print("Not an integer", type(userdata))
            self.cur.execute(f"DELETE FROM users WHERE id= {userdata['id']}")
            print(userdata['id']);
            if self.cur.rowcount>0:
                return make_response({"message":"User data deleted successfully"}, 201)
            else:
                return make_response({"message":"Nothing to delete"}, 204)
    