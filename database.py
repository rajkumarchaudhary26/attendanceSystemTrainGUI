import mysql.connector
import datetime


def database():
    db = mysql.connector.connect(
        host="localhost", user="root", password="", db="attendance")
    return db


def addStudent(db, firstName, LAstName, Email, Address):
    now = datetime.datetime.now()
    currentDate = now.strftime("%Y-%m-%d")
    cursor = db.cursor()
    sql = "INSERT INTO AttendanceApp_student(first_name,last_name, email, address,created_date,updated_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(
        firstName, LAstName, Email, Address, currentDate, currentDate)
    cursor.execute(sql)
    db.commit()
    # db.close()


def fetch_data():
    db = mysql.connector.connect(
        host="localhost", user="root", password="", db="attendance")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "select id,first_name from AttendanceApp_student"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()[-1]
        id = results[0]
        name = results[1]
        return id, name
    except:
        print("Error: unable to fetch data")

        # disconnect from server
    db.close()
