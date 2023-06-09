import sys
import sqlite3 
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
	print("I expect a single argument, the name of the file that contains the bookmaks.html.")
	sys.exit(0)

conn = sqlite3.connect('bookmarks.db') 
c = conn.cursor()

def table_exists(): 
    c.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = 'bookmarks' ''') 
    if c.fetchone()[0] == 1: 
        return True 
    return False

if not table_exists(): 
    c.execute(''' 
        CREATE TABLE bookmarks( 
            title TEXT, 
            url TEXT, 
            tags TEXT 
        ) 
    ''')


HTMLFile = open(sys.argv[1], "r")

index = HTMLFile.read()

S = BeautifulSoup(index, 'lxml')

for tag in S.find_all('a'):
	print(f'{tag.text} * {(tag.attrs)["href"]}')
	c.execute(''' INSERT OR REPLACE INTO bookmarks (title, url, tags) VALUES(?, ?, ?) ''', (tag.text, (tag.attrs)["href"], "")) 
	conn.commit()



# Links
# https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
# https://towardsdatascience.com/python-has-a-built-in-database-heres-how-to-use-it-47826c10648a
