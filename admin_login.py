from setup import * 
from tkinter import messagebox
from admin import *

#Frames
#Admin
Admin_login = Frame(window)
Admin_login.pack(side=RIGHT)
Admin_login.pack_propagate(False)
Admin_login.configure(width=1000,height=600)
Admin_login.pack_forget()

def printInput():
    username_entry_data = username_entry.get()
    password_entry_data = password_entry.get()
    password_bytes = password_entry_data.encode("utf-8")

    if username_entry_data == username:
        result = bcrypt.checkpw(password_bytes, hash)
        if result:
            print("username :",username_entry_data,"Logged in successfully")
            Admin_login.pack_forget()
            login_access(result)
        else:
            messagebox.showerror("Password", "password does not match")
    else:
        messagebox.showerror("Username", "username does not exist")
canvas_admin = Canvas(
    Admin_login,
    bg = "#0c0c0c",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_admin.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Assets\Admin\Register/background.png")
background = canvas_admin.create_image(
    500.0, 300.0,
    image=background_img)

entry_img = PhotoImage(file = f"Assets\Admin\Register/textbox_img.png")
username_entry_bg = canvas_admin.create_image(
    494.5, 230.5,
    image = entry_img)

username_entry = Entry(
    Admin_login,
    bd = 0,
    bg = "#d9d9d9",
    font=('Arial 18'),
    highlightthickness = 0)

username_entry.place(
    x = 303.0, y = 198,
    width = 383.0,
    height = 63)

password_entry = Entry(
    Admin_login,
    bd = 0,
    bg = "#d9d9d9",
    font=('Arial 18'),
    show = "*",
    highlightthickness = 0)

password_entry.place(
    x = 303.0, y = 311,
    width = 383.0,
    height = 63)

password_entry_bg = canvas_admin.create_image(
    494.5, 343.5,
    image = entry_img)


img0 = PhotoImage(file = f"Assets\Admin\Register\submit_btn.png")
submit_btn = Button(
    Admin_login,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = printInput,
    relief = "flat")

submit_btn.place(
    x = 385, y = 424,
    width = 219,
    height = 65)
