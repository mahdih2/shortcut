import sqlite3

def create_db():
    con = sqlite3.connect('shortcut/Mahdi.db')
    cur = con.cursor()
    return con, cur