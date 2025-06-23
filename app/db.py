import sqlite3
import os
from flask import g

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def db_backup(name):
    destination = "databaseBackup"
    os.makedirs(destination, exist_ok=True)
    backup = os.path.join(destination, f"Backup-{name}.db")
    con = get_connection()
    con.backup(sqlite3.connect(backup))
    con.close()