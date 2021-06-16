# import
import sqlite3



def register_user():
    connection = sqlite3.connect('dept')
    connection.execute(
        "INSERT INTO student( " +
        "student_id, user_name, "
        "first_name, last_name, "
        "gender, age, school_level, "
        "reg_no) "
        "VALUES ( ?, ?, ?, ?, ?, ?, ?, ? );")
    connection.commit()
    connection.close()

def find_user():
    connection = sqlite3.connect('dept')
    res = connection.execute("SELECT ")
