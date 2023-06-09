import sys
import sqlite3 

if len(sys.argv) != 3:
	print("I expect a two arguments, the pattern to match and the tags to update the matched records.")
	sys.exit(0)

pattern = sys.argv[1]
newTags = sys.argv[2]

conn = sqlite3.connect('bookmarks.db') 
c = conn.cursor()
c.execute(f"UPDATE bookmarks SET tags = tags || ', {newTags}' WHERE url LIKE '%{pattern}%'")
conn.commit()