from setup import *
from admin_login import *
import Matplotlib
import math

def graph():
    Matplotlib.Graph_1()

def Menu_btn_clicked(page):
    page_indicator.config(text=page)
    Admin_page = ".!frame"
    Library_info_page = ".!frame5"
    Book_showcase_page = ".!frame6"
    Admin_login_page = ".!frame3"
    Admin_page_contents= ".!frame2"
    
    if page == "Demographics":
        graph()
    if page == "Admin":
        page = Admin_login_page
    if page == "My Library":
        page = Library_info_page
    if page == "Demographics":
        page = Library_info_page
    for frames in window.winfo_children():
        if str(frames) == page:
            print(frames)
            frames.pack(side=RIGHT)
        elif str(frames) in [Admin_page, Library_info_page,Book_showcase_page,Admin_login_page,Admin_page_contents]:
            frames.pack_forget()
        else:
            print(frames)
            print("ERROR: Page Not Found")
            
def Category_btn_clicked(m,n,name):
    print(name)
    Location = Books["Location"]
    Book_Category = Books["Book_name"]
    Library_info.pack_forget()
    Book_showcase.pack(side=RIGHT)
    s.place(x=436,y=21)
    s.config(text=name)
    print("Button Clicked",m,n,name)

def category_page_controller(towards):
    global e_category
    global current_category_page
    category_page_division = len(category)/9
    if category_page_division <= 1:
        category_page_total = 1

    if category_page_division > 1:
        category_page_total = math.ceil(category_page_division)

    category_location = Books["Location"]
    category_organised = [category[i:i + 9] for i in range(0, len(category), 9)]
    location_organised = [category_location[i:i + 9] for i in range(0, len(category_location), 9)]

    if towards == "same":
        current_category_page = 1
        current_category_page_pos = current_category_page-1
        category_page_contents(category_organised,current_category_page_pos,location_organised)

    if towards == "next":
        if current_category_page < category_page_total:
            current_category_page += 1
            current_category_page_pos = current_category_page-1
            category_page_contents(category_organised,current_category_page_pos,location_organised)
        else:
            pass 

    if towards == "prev":
        if current_category_page > 1:
            current_category_page -= 1
            current_category_page_pos = current_category_page-1
            category_page_contents(category_organised,current_category_page_pos,location_organised)
        else:
            pass



def category_page_contents(category_organised,current_category_page_pos,location_organised):
    m=1
    n=1
    x = 70
    y = 172
    i = 0
    max_m,max_n = 3,3
    for widgets in Library_info.winfo_children():
        if str(widgets).startswith(".!frame3.!button") or str(widgets).startswith(".!frame3.!label"):
            if str(widgets) == ".!frame3.!button10" or str(widgets) == ".!frame3.!button11":
                pass
            else:
                widgets.destroy()
    while m <= max_m and n <= max_n:
        if i < len(category_organised[current_category_page_pos]):
            e_category = Button(
            Library_info,
            image = rack_img,
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda m=m,n=n,name=category_organised[current_category_page_pos][i]: Category_btn_clicked(m,n,name),
            compound = LEFT, 
            relief = "flat")
            e_category.place(
                x = x, y = y,
                width = 286,
                height = 98)
            category_label = Label(Library_info, text=f"{category_organised[current_category_page_pos][i]} ({location_organised[current_category_page_pos][i]})",bg="#D36B02",font=("Arial", 16),fg="#FFFFFF",bd=0)
            category_label.place(x=x+20,y=y+20)
            category_label.bind("<Button-1>",lambda e, m=m,n=n,name=category_organised[current_category_page_pos][i]:Category_btn_clicked(m,n,name) )
            i += 1
            if n == max_n:
                m += 1
                n = 1
                y += 128
                x = 70
            else:
                n += 1
                x += 294
        else:
            break
def Book_showcase_btn_clicked():
    print("Button Clicked")

def Back_button_clicked():
    Book_showcase.pack_forget()
    Library_info.pack(side=RIGHT)
    print("Back page")

#Frames
#Menu Bar
Menu_bar = Frame(window)
Menu_bar.pack(side=LEFT)
Menu_bar.pack_propagate(False)
Menu_bar.configure(width=200, height=600)


#Library_info
Library_info = Frame(window)
Library_info.pack(side=RIGHT)
Library_info.pack_propagate(False)
Library_info.configure(width=1000,height=600)

#Books_showcase
Book_showcase = Frame(window)
Book_showcase.pack(side=RIGHT)
Book_showcase.pack_propagate(False)
Book_showcase.configure(width=1000,height=600,background="#0C0C0C")
Book_showcase.pack_forget()

#Menubar_contents
canvas_Menubar = Canvas(
    Menu_bar,
    bg = "#1e1e1e",
    height = 600,
    width = 200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_Menubar.place(x = 0, y = 0)

page_indicator = Label(Menu_bar, text="Home",bg="#027BD3",font=("Arial", 18),fg="#FFFFFF",bd=0,padx=5,pady=5)
page_indicator.place(x=14,y=30)

inactive_btn_img = PhotoImage(file = f"Assets\Menu_bar\inactive_btn_img.png")
pages = ["Admin","My Library","Demographics"]
x,y = 14,140

for page in pages:
    batn = Button(
        Menu_bar,
        image = inactive_btn_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda page=page: Menu_btn_clicked(page),
        relief = "flat").place(
        x = x, y = y,
        width = 172,
        height = 59)
    print(page)
    label = Label(Menu_bar, text=f"{page}",bg="#D36B02",font=("Arial", 16),fg="#FFFFFF",bd=0)
    label.place(x=x+20,y=y+14)
    label.bind("<Button-1>",lambda e, page=page:Menu_btn_clicked(page) )
    y += 70

#Library_info_contents
canvas_Library_info = Canvas(
    Library_info,
    bg = "#0c0c0c",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_Library_info.place(x = 0, y = 0)

background_Library_info_img = PhotoImage(file = f"Assets\Library_info/background.png")
background = canvas_Library_info.create_image(
    500.0, 300.0,
    image=background_Library_info_img)

rack_img = PhotoImage(file = f"Assets\Library_info\Rack(container).png")
category = Books["Category"]

nxt_btn_img = PhotoImage(file = f"Assets\Library_info/next_btn_img.png")
prev_btn_img = PhotoImage(file = f"Assets\Library_info\prev_btn_img.png")
category_page_controller("same")
nxt_btn = Button(
    Library_info,
    image = nxt_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda towards="next":category_page_controller(towards),
    relief = "flat")

nxt_btn.place(
    x = 871, y = 120,
    width = 46,
    height = 46)

prev_btn = Button(
    Library_info,
    image = prev_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda towards="prev":category_page_controller(towards),
    relief = "flat")

prev_btn.place(
    x = 809, y = 120,
    width = 46,
    height = 46)

#Book_showcase_contents
canvas_Bookshowcase = Canvas(
    Book_showcase,
    bg = "#0c0c0c",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_Bookshowcase.place(x = 0, y = -7)

background_Bookshowcase_img = PhotoImage(file = f"Assets\Book_info/background.png")
background_Bookcase = canvas_Bookshowcase.create_image(
    500.0, 288.5,
    image=background_Bookshowcase_img)

s =Label(Book_showcase, text="None",bg="#0099FF",font=("Arial", 32),fg="#FFFFFF",bd=0,padx=5,pady=5)

Book_showcase_btn_img = PhotoImage(file = f"Assets\Book_info/book_button.png")
Book_showcase_btn = Button(
    Book_showcase,
    image = Book_showcase_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = Book_showcase_btn_clicked,
    relief = "flat")

Book_showcase_btn.place(
    x = 78, y = 147,
    width = 213,
    height = 59)

Back_button_img = PhotoImage(file = f"Assets\Book_info\Back_btn_img.png")
b2 = Button(
    Book_showcase,
    image = Back_button_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = Back_button_clicked,
    relief = "flat")

b2.place(
    x = 9, y = 15,
    width = 61,
    height = 61)

window.resizable(False, False)
window.mainloop()
