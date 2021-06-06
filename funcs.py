import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def db_strip(text):
    str(text).strip("[]()'',")

def insert_weapon(username, wep_name):
    query = "INSERT INTO {}_weapons VALUES('{}')".format(username, wep_name)
    c.execute(query)