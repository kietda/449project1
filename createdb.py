import sqlite3

conn = sqlite3.connect('project1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER UNIQUE, title TEXT, text TEXT, community TEXT, url TEXT, username TEXT, date TEXT)')
    #conn.commit()
    #c.close()
    #conn.close()

#test, delete later
def data_entry():
    c.execute('INSERT INTO posts VALUES(1, "Buy groceries", "Milk", "Sales", "http://walmart.com","tester1","03/01/2020")')
    c.execute('INSERT INTO posts VALUES(2, "Learn Python", "Need to find a good Python tutorial on the web", "Technology", "https://miro.medium.com/max/768/1*CrK1VuTTMSg-zL9-z3ohQQ.png","tester2","03/02/2020")')
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()