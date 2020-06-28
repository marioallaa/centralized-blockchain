from chain import *
from flask import Flask, request
import json

c = Chain()
app = Flask(__name__)

@app.route('/readAll')
def returnAllData():
    return {"chainContent": c.returnData}

@app.route('/')
def home():
    return {
                "greeting": "welcome",
                "GET Requests":
                    [
                        {
                            "/readAll": "returns all data on the blockchain",
                            "/mine?payload=<value>": "saves value on the blockchain"
                        }
                    ]
            }, 200

@app.route('/mine')
def mine():
    l = c.mine(payload=request.args.get('payload'))
    return f'mined: {l}'

app.run(host='0.0.0.0', port=10035)