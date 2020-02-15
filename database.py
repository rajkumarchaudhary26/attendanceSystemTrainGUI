import MySQLdb
import datetime
def database():
    db = MySQLdb.connect("localhost","root","","attendance" )
    return db

def addStudent(db,firstName,LAstName,Email,Address):
    now = datetime.datetime.now(); 
    currentDate = now.strftime("%Y-%m-%d")
    cursor = db.cursor()
    sql = "INSERT INTO attendanceapp_student(first_name,last_name, email, address,created_date,updated_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(firstName,LAstName,Email,Address,currentDate,currentDate)
    cursor.execute(sql)
    db.commit()


def fetch_data():
    db = MySQLdb.connect("localhost","root","","attendance")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT id,first_name FROM attendanceapp_student"
    try:
        # Execute the SQL command
        cursor.execute(sql)
            # Fetch all the rows in a list of lists.
        results = cursor.fetchall()[-1]
        id = results[0]
        name = results[1]
        return id,name
    except:
        print ("Error: unable to fecth data")

        # disconnect from server
    db.close()