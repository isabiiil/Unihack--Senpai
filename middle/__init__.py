from flask import *
import json

app = Flask(__name__)
app.secret_key = "debug"

@app.route("/")
def my_index():
    return render_template("index.html", json_data=json.dumps({"mood":"doof"}))

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

@app.route("/mood", methods=["GET"])
def mood():
    return "hello"


if __name__ == "__main__":
	app.run(debug=True, port=5001)
