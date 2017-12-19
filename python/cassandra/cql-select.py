import cql
con = cql.connect('system_schema', 9160,  '', cql_version='3.0.0')
print ("Connected!")
cursor = con.cursor()
CQLString = "select * from tables;"
cursor.execute(CQLString)
