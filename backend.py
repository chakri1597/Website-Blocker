import sqlite3


def insert(site="",redirect=""):

    conn = sqlite3.connect("Testing.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Blocked_sites (site varchar PRIMARY KEY ,redirect_to varchar )")
    cur.execute("INSERT  INTO Blocked_sites VALUES (?,?)",(site,redirect,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Testing.db")
    cur = conn.cursor()
    cur.execute("SELECT Site FROM Blocked_sites ")
    columns=cur.fetchall()
    conn.commit()
    conn.close()
    return columns

def delete(site):
    conn = sqlite3.connect("Testing.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Blocked_sites WHERE site=?",(site))
    conn.commit()
    conn.close()




