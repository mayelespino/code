import sys
import sqlite3 

conn = sqlite3.connect('bookmarks.db') 
c = conn.cursor()

c.execute('''SELECT * FROM bookmarks''') 
for row in c.fetchall(): 
    print(row)
