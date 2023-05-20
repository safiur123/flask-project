from flask import Flask, jsonify
import os

app = Flask(__name__)
#message = { "id" : "1", "message": "Hello World!" }

@app.route("/")
def hello_world():
     return jsonify(
         id="1",message="Hello world")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

