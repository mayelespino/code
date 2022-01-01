import pymysql

def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='meantsle.local',
        port=22016,
		user='root',
		password = "12@Elefantes",
		db='mysql',
		)
	
	cur = conn.cursor()
	cur.execute("select @@version")
	output = cur.fetchall()
	print(output)
	
	# To close the connection
	conn.close()

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()

