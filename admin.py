from setup import *

def login_access(result):
    if result:
        Admin = Frame(window)
        Admin.pack_propagate(False)
        Admin.configure(width=1000,height=600)
        Admin.pack(side=RIGHT)
        print("Hello")
        def btn_clicked():
            print("Button Clicked")
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
            command = btn_clicked,
            relief = "flat")

        Books_btn.place(
            x = 19, y = 90,
            width = 315,
            height = 67)
    else:
        print("Login to access admin")
    window.resizable(False, False)
    window.mainloop()