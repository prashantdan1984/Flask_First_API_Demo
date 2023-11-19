#import mysql.connector  #then write mysql.connector.connect
import mysql.connector as mysql # then write mysql.connect
import json
class user_model():
    def __init__(self):
        try:
            #Connection establishment code.
            #connection = mysql.connect(host="localhost", user="root", port='3306', password="12345", database="flask_demo")
            #con=mysql.connecter.connect(user="root", password="12345", host="localhost", database="flask_demo")
            self.con=mysql.connect(user="root", password="12345", host="localhost", database="flask_demo")
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
            return json.dumps(result)
        else:
            return "No Data Found"
        #return "This is user signup model4" + " " +name