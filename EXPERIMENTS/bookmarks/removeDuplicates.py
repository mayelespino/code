import sys
import sqlite3 

conn = sqlite3.connect('bookmarks.db') 
c = conn.cursor()
c.execute('''delete from bookmarks where rowid not in (select min(rowid) from bookmarks group by url)''')
conn.commit()