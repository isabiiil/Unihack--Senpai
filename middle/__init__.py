from flask import *

app = Flask(__name__)
app.secret_key = "debug"

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