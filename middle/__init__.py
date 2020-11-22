from flask import *
import requests
import json
import uuid
import time

app = Flask(__name__)
app.secret_key = "debug"


def gimmetoken():
    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/auth"

    payload = "{\"username\":\"moody\",\"password\":\"Moody921\"}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fd91ccce-5703-4cde-ab48-9bee17b2daba"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)

    rj = json.loads(response.text)

    # print (rj['authToken'])

    return rj['authToken']


def registeruser(username, pw, imgurl):
	
    utoken = str(uuid.uuid4())
    time.sleep(1)
    utoken2 = str(uuid.uuid4())

    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/data/tables/users/rows"

    atoken = gimmetoken()

    payload = {}
    pc = []
    pc.append({"name":"id","value":utoken})
    pc.append({"name":"name","value":username})
    pc.append({"name":"password","value":pw})
    pc.append({"name":"avatar","value":imgurl})

    payload ['columns'] = pc

    jpayload = json.dumps(payload)

    # payload = "{\"columns\":[,,,]}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'x-cassandra-request-id': utoken2,
        'x-cassandra-token': atoken,
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=jpayload, headers=headers)

    return response.text




@app.route("/", methods=["GET"])
def index():
	return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		data = request.json
		
		if ("uname" not in data) or ("pw0" not in data) or ("pw1" not in data):
			return {"status":"bad json"}
		
		if data["pw0"] != data["pw1"]:
			return {"status":"Password's must match"}

		return {"status":"User registered"}
	else:
		return render_template("register.html")

@app.route("/auth", methods=["POST"])
def auth():

	return request.json

if __name__ == "__main__":
	app.run()
