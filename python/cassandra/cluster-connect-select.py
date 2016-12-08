from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('excelsior')
rows = session.execute('SELECT * FROM mytable')
for row in rows:
    print row, row.mykey, row.myvalue