from tkinter import *
import bcrypt
#window1
window = Tk()
window.geometry("1200x600")
window.configure(bg = "#000000")
window.title("My Library")


#Global Variables

Books = {"Book_name":[],
        "Category":["School Books","Adventure","Fantasy","Sci-Fi","Mystery","Thriller","Romance","Romance","Romance","Romance","Romance"],
        "Location":[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(5,1),(5,2),(5,3)],
        "Description":[]}

#Login Management
password = "Hello"
username = "GIIS-Lib"
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
print(hash)