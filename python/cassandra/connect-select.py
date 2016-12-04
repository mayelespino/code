import cql
con = cql.connect('159.203.107.80', 9160,  'Excelsior', cql_version='3.0.0')
print ("Connected!")
cursor = con.cursor()
CQLString = "select * from mytable;"
cursor.execute(CQLString)
