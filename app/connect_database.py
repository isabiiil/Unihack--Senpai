from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


cloud_config= {
        'secure_connect_bundle': 'secure-connect-unihack2020.zip'
}
auth_provider = PlainTextAuthProvider('REPLACE THIS WITH USERNAME', 'PASSWORD HERE')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")