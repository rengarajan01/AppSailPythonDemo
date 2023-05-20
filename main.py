from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "GET":
        return "Return From GET Method"
    elif request.method == "POST":
        return "Return From POST Method"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["X_ZOHO_CATALYST_LISTEN_PORT"])