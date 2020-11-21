
from flask import *
from urllib.request import *
from os import environ
app = Flask(__name__)
header={
	"content-type":"application/json",
	"x-cassandra-token":environ["ASTRA_AUTHORIZATION_TOKEN"]
}



@app.route("/", methods=["GET"])
def index():

	return render_template("index.html")


@app.route("/astratest", methods=["GET"])
def mood():
	'''
	curl --request POST \
    --url https://${ASTRA_CLUSTER_ID}-${ASTRA_CLUSTER_REGION}.apps.astra.datastax.com/api/rest/v1/keyspaces/${ASTRA_DB_KEYSPACE}/tables \
    --header 'content-type: application/json' \
    --header "x-cassandra-token: ${ASTRA_AUTHORIZATION_TOKEN}" \
    --data '{"name":"mood"}'
	'''

	return header


if __name__ == "__main_":
	app.run()
