import sqlite3

_conn = sqlite3.connect('imc.db')

def conn():
    return _conn
    
def cursor():
    return _conn.cursor()

def close():
    _conn.close()
