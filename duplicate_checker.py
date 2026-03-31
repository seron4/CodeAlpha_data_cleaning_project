import sqlite3

def is_duplicate(email):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records WHERE email=?", (email,))
    result = cursor.fetchone()

    conn.close()
    return result is not None
