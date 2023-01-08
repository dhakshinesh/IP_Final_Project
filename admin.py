from setup import *
from tkinter import messagebox
import Models
import Show_details
import os

def login_access(result):
    if result:
        Admin.pack(side=RIGHT)
        Admin_Content.place(x=228,y=164)
        def btn_clicked():
            print("Btn_clicked")
        def Add_changes():
            messagebox.showinfo(title="Added changes", message=Models.add_init_values())
            update_books()
        def Modify_changes():
            messagebox.showinfo(title="Modified changes", message=Models.add_init_values())
            update_books()
        def Open_excel_book():
            os.startfile('Assets\Excel\Books.csv')
        def Details():
            Show_details.show_details()
        canvas = Canvas(
              Admin_Content,
              bg="#FFFFFF",
              height=371,
              width=943,
              bd=0,
              highlightthickness=0,
              relief="ridge")
        canvas.place(x=0, y=0)

        content_background_img = PhotoImage(
              file=f"Admin_assets\Assets\Admin_contents/background.png")
        content_background = canvas.create_image(
              473.0, 217.5,
              image=content_background_img)

        add_btn_img = PhotoImage(
              file=f"Admin_assets\Assets\Admin_contents\img0.png")
        add_btn = Button(
              Admin_Content,
              image=add_btn_img,
              borderwidth=0,
              highlightthickness=0,
              command=btn_clicked,
              relief="flat")

        add_btn.place(
              x=32, y=278,
              width=214,
              height=60)

        details_btn_img = PhotoImage(
              file=f"Admin_assets\Assets\Admin_contents\img1.png")
        details_btn = Button(
              Admin_Content,
              image=details_btn_img,
              borderwidth=0,
              highlightthickness=0,
              command=Details,
              relief="flat")

        details_btn.place(
              x=32, y=196,
              width=214,
              height=60)

        img2 = PhotoImage(
              file=f"Admin_assets\Assets\Admin_contents\img2.png")
        b2 = Button(
              Admin_Content,
              image=img2,
              borderwidth=0,
              highlightthickness=0,
              command=Modify_changes,
              relief="flat")

        b2.place(
              x=32, y=114,
              width=214,
              height=60)

        img3 = PhotoImage(
              file=f"Admin_assets\Assets\Admin_contents\img3.png")
        b3 = Button(
              Admin_Content,
              image=img3,
              borderwidth=0,
              highlightthickness=0,
              command=Add_changes,
              relief="flat")

        b3.place(
              x=32, y=32,
              width=214,
              height=60)
        
        canvas = Canvas(
            Admin,
            bg = "#f0e3ca",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Admin_assets\Assets\Admin_home/background.png")
        background = canvas.create_image(
            500.0, 305.0,
            image=background_img)

        img0 = PhotoImage(file = f"Admin_assets\Assets\Admin_home\settings_btn.png")
        b0 = Button(
            Admin,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 665, y = 90,
            width = 315,
            height = 67)

        img1 = PhotoImage(file = f"Admin_assets\Assets\Admin_home\students_btn.png")
        b1 = Button(
            Admin,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b1.place(
            x = 334, y = 90,
            width = 331,
            height = 67)

        img2f = PhotoImage(file = f"Admin_assets\Assets\Admin_home\Books_btn.png")
        Books_btn = Button(
            Admin,
            image = img2f,
            borderwidth = 0,
            highlightthickness = 0,
            command = Open_excel_book,
            relief = "flat")

        Books_btn.place(
            x = 19, y = 90,
            width = 315,
            height = 67)
    else:
        print("Login to access admin")
    window.resizable(False, False)
    window.mainloop()
