#!/usr/bin/python3.4
from flask import Flask, request
import os
import urllib.request
app = Flask(__name__)
url = "http://print-hello-world-svc:5000"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_content = response.read()
reverse_content = data_content[::-1]
@app.route("/")
def hello():
    return reverse_content
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0',port=port)

