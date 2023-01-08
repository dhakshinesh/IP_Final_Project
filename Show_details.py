import Models
from setup import *


def show_details():
            window_details = Toplevel(window)
            window_details.geometry("400x400")
            window_details.configure(bg = "#000000")
            window_details.title("My Library")
            T = Text(window_details, height = 400, width = 400,spacing2=10)
            details = str(Models.db.select_from_table("Books"))
            T.pack()
            T.insert(END, details)
            T.config(state=DISABLED)
            window_details.mainloop()