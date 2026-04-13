import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SECURITY ISSUE: SQL Injection — user input is concatenated directly into query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print(get_user("admin"))

