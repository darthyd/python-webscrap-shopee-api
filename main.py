from flask import Flask, request
from json import dumps
from src import webscrap
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/search')
def search():
    query = request.args.get('query')
    resp = webscrap.getData(query)
    return dumps(resp)
