import sys
import sqlite3 

conn = sqlite3.connect('bookmarks.db') 
c = conn.cursor()
c.execute('''SELECT DISTINCT * FROM bookmarks''') 

print("<html><body>")
count = 0
for row in c.fetchall(): 
    (title, url, tags) = row
    count += 1
    print(f'{count} <a href="{url}" target="_blank">{title}</a><br/>{tags}<br/><br/>\n')
print("</body></html>")