from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	return render_template("home.html")

if __name__ == "__main__":
	app.run()