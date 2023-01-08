#This is a library file, do not run separately.
from setup import database
import pandas as pd
mycur = database.db.cursor()
con = database.db.connect()

#Functions
#tables() ---> Creates tables if it does not exist already *Runs all the time(whenever file is executed)*
#show_tables() ---> Shows all the tables in the database
#insert_into_Person(name,age) ---> Adds another record to Person table. *requires name,age argument*
#select_from_table(table_name) ---> Selects records from given table. *requires table_name argument*
#desc_table ---> Describes all the tables
def tables():
        try:
            mycur.execute("CREATE TABLE IF NOT EXISTS admin(name varchar(10),password varchar(10))")
            mycur.execute("CREATE TABLE IF NOT EXISTS Person(name varchar(10),password varchar(10))")
            mycur.execute("CREATE TABLE IF NOT EXISTS Books(Book_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,Book_name varchar(255) NOT NULL,Book_category varchar(100) NOT NULL,Book_pos1 int NOT NULL,Book_pos2 int NOT NULL)")
        except:
            print("ERROR CREATING TABLES")
def show_tables():
        mycur.execute("SHOW TABLES")
        lst = []

        for x in mycur:
            lst.append(x)
        return lst

def add_init_values():
    message = "No changes made"
    mycur.execute("SELECT Book_name,Book_category,Book_pos1,Book_pos2 FROM Books")
    Books_db_lst = []
    
    for x in mycur:
        Books_db_lst.append(x)
    Books_excel = pd.read_csv("E:/Dhakshinesh/ClassXII/IP Project/Final/Github_Main/IP_Final_Project/Assets/Excel/Books.csv")

    Books_db_ids = []
    mycur.execute("SELECT Book_id FROM Books")
    for x in mycur:
        x = int(''.join(map(str, x)))
        Books_db_ids.append(x)

    Books_excel_lst = []
    for index,row in Books_excel.iterrows():
        l = (row[1],row[2],row[3],row[4])
        Books_excel_lst.append(l)

        if row[0] not in Books_db_ids:
            message = "Added new element(s)"
            if l not in Books_db_lst:
                mycur.execute("INSERT INTO Books(Book_name,Book_category,Book_pos1,Book_pos2) VALUES(%s,%s,%s,%s)",l)
                database.db.commit()
    #checking for updates
    for x,y in zip(Books_db_lst,Books_excel_lst):
        if x[0] != y[0]:
            mycur.execute("UPDATE Books SET Book_name = %s WHERE Book_name = %s",(y[0],x[0]))
            database.db.commit()
            message = "Book_name is changed"
        if x[1] != y[1]:
            mycur.execute("UPDATE Books SET Book_category = %s WHERE Book_name = %s",(y[1],x[0]))
            database.db.commit()
            message = "Book_category is changed"
        if x[2] != y[2]:
            mycur.execute("UPDATE Books SET Book_pos1 = %s WHERE Book_name = %s",(y[2],x[0]))
            database.db.commit()
            message = "Book_pos1 is changed"
        if x[3] != y[3]:
            mycur.execute("UPDATE Books SET Book_pos2 = %s WHERE Book_name = %s",(y[3],x[0]))
            database.db.commit()
            message = "Book_pos2 is changed"
    return message

class db_functions:
    def __init__(self):
        pass

    def select_from_table(self,table_name):
        mycur.execute(f"SELECT * FROM {table_name}")
        result = []
        for x in mycur:
            print(x)
            result.append(x)
        return result

    def category_graph(self):
        mycur.execute("SELECT COUNT(Book_name),Book_category FROM Books GROUP BY Book_Category")
        result = []
        for x in mycur:
            result.append(x)
        return result

#Default
tables() #checks if table exists
add_init_values()
db = db_functions()
#user1.insert_into_Person()
db.select_from_table("Books")
