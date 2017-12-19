from cassandra.cluster import Cluster

cluster = Cluster(['10.0.1.40'],port=9042)
session = cluster.connect()
session.set_keyspace('system_schema')
rows = session.execute('SELECT * FROM tables')
for row in rows:
    print row
