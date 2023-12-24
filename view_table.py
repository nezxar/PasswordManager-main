from tkinter import ttk
import tkinter as tk
import sqlite3

def connect():
    con = sqlite3.connect("<path/database_name>")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    con.commit()
    con.close()

def View(root: tk.Tk | tk.Frame | ttk.Frame):
    tree = ttk.Treeview(root, columns=("c1", "c2", "c3", "c4", "c5"), show='headings')
    tree.column("#1", anchor=tk.CENTER, width=8)
    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Encrypted Password")

    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Encrypted Email")

    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Encrypted Site Name")

    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Encryption Type")
    tree.pack()

    con = sqlite3.connect("nizar_database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM user_info")
    rows = cur.fetchall()    
    for row in rows:
        # print(row) 
        tree.insert("", tk.END, values=row)        
    con.close()