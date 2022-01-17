import sqlite3

con = sqlite3.connect('SavedCredentials.db')

cur = con.cursor()

class DBtable:
    def __init__(self, type, username, password):
        self.type = type
        self.username = username
        self.password = password
        self.table = '''CREATE TABLE IF NOT EXISTS 
        UserPassInfo (type TEXT, username TEXT, password TEXT)'''
        cur.execute(self.table)
        self.Table_result = cur.execute("SELECT * FROM UserPassInfo")
        con.commit()

    def add(self):
        if self.type and self.username and self.password:
            cur.execute("INSERT INTO UserPassInfo (type, username, password) VALUES ('%s','%s','%s')"
                        %(self.type, self.username, self.password))
            con.commit()
