import sqlite3

_conn = sqlite3.connect('../db/imc.db')

def conn():
    return _conn

def close():
    _conn.close()
