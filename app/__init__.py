
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




if __name__ == "__main_":
	app.run()
