from cassandra.cluster import Cluster

KEYSPACE="user_key_space_2"

cluster = Cluster(['10.0.1.40'])
session = cluster.connect()
rows = session.execute("SELECT keyspace_name FROM system_schema.keyspaces")
if KEYSPACE in [row[0] for row in rows]:
    print("Keyspace {} already exists".format(KEYSPACE))
else:
    print("Creating keyspace {}".format(KEYSPACE))
    session.execute("CREATE KEYSPACE {} WITH replication = { \'class\': \'SimpleStrategy\', 'replication_factor\': \'3\' }".format(KEYSPACE)) 
#
session.shutdown()
