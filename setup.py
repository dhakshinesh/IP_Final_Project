from tkinter import *
import bcrypt
import mysql.connector

#window1
window = Tk()
window.geometry("1200x600")
window.configure(bg = "#000000")
window.title("My Library")
#test
Admin = Frame(window)
Admin.pack_propagate(False)
Admin.configure(width=1000,height=600)

Admin_Content = Frame(window)
Admin_Content.pack_propagate(False)
Admin_Content.configure(width=940,height=370)

#Global Variables

Books = {"Book_name":[],
        "Category":[],
        "Location":[]}

#Login Management
password = "Hello"
username = "GIIS-Lib"
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
print(hash)

#database
class database():
    db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="User@290",
    database="testdatabase"
    )

temp_cur = database.db.cursor()

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
    
def update_books():
    temp_cur.execute("SELECT Book_name from Books")
    for x in temp_cur:
        Books["Book_name"].append(convertTuple(x))
    temp_cur.execute("SELECT Book_category from Books GROUP BY Book_Category")
    for x in temp_cur:
        Books["Category"].append(convertTuple(x))
    #location
    loc1_lst = []
    temp_cur.execute("SELECT Book_Pos1 from Books")
    for x in temp_cur:
        loc1_lst.append(x)
    loc2_lst = []
    temp_cur.execute("SELECT Book_Pos2 from Books")
    for x in temp_cur:
        loc2_lst.append(x)

    for x,y in zip(loc1_lst,loc2_lst):
        x = int(''.join(map(str, x)))
        y = int(''.join(map(str, y)))
        if (x,y) not in Books["Location"]:
            Books["Location"].append((x,y))
update_books()