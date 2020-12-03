# import the libraries
import sqlite3
import pandas as pd

# create a connection
con = sqlite3.connect('project1_quiz_cs384.db')

# read data from SQL to pandas dataframe.
data = pd.read_sql_query('Select * from project1_marks;', con)

print(data)

# c = con.cursor()
# # read data from SQL to pandas dataframe.
# c.execute("DELETE from userinfo WHERE name = ?", ['Yuvi'])
# con.commit()
# con.close()


# import tkinter
# from tkinter import *
# global root
# root = Tk()
# global i


# def change():
#     global i
#     i -= 1
#     return


# for i in range(60):
#     l = Label(root)
#     l.place(relx=0.5, rely=0.5)
#     root.after(1000, lambda x: l['text']=x-1, i)

# root.mainloop()


# conn = sqlite3.connect("project1 quiz cs384.db")
# c = conn.cursor()

# c.execute(""" CREATE TABLE project1_registration(
#           name text,
#           roll text,
#           phone text,
#           password text
#           )""")

# conn.commit()

# conn.close()

# conn = sqlite3.connect("project1 quiz cs384.db")
# c = conn.cursor()

# c.execute(""" CREATE TABLE project1_marks(
#           roll text,
#           quiz_num text,
#           total_marks text
#           )""")

# conn.commit()

# conn.close()
