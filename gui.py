import tkinter
window = tkinter.Tk('Training')
import os
from  dataset import index
from database import addStudent,database,fetch_data
from traning import training


def submit():
    fName = fn.get()
    lName = ln.get()
    emailAddress = email.get()
    address = cAddress.get()
    # try:
    db =  database()
    addStudent(db,fName,lName,emailAddress,address)
    id,name = fetch_data()
    path = 'C:/Users/Raj/Desktop/dataset/{}/'.format(id)
    os.mkdir(path)
    index(path)
    
    # except:
    #     print("Error")
    

lblFirstName = tkinter.Label(window,text="First Name").place(x=0,y=0)
fn = tkinter.StringVar()
entryFirstName = tkinter.Entry(window,textvar=fn).place(x=70,y=0)

lblLastName = tkinter.Label(window,text="Last Name").place(x=0,y=40)
ln = tkinter.StringVar()
entryLastName = tkinter.Entry(window,textvar=ln).place(x=70,y=40)

lblEmail = tkinter.Label(window,text="Email").place(x=0,y=80)
email = tkinter.StringVar()
entryEmail = tkinter.Entry(window,textvar=email).place(x=70,y=80)
cAddress = tkinter.StringVar()
lblAddress = tkinter.Label(window,text="Address").place(x=0,y=120)
entryAddress = tkinter.Entry(window,textvar=cAddress).place(x=70,y=120)


button = tkinter.Button(window,text='Submit',command=submit).place(x=170,y=190)
button = tkinter.Button(window,text='Train',command=training).place(x=230,y=190)
window.geometry('500x500')
window.mainloop()

