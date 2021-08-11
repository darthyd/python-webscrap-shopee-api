import os
from flask import Flask, request
from json import dumps
from src import webscrap
app = Flask(__name__)

@app.route('/')
def home():
    doc = '\n\
{\n\
  "api":\n\
    {\n\
      "name": "Webscrap Shopee",\n\
      "endpoints":\n\
         { \n\
           "search": "/api/search?query=KEY OF SEARCH", \n\
         }, \n\
      "author": "Lucas Oliveira",\n\
    },\n\
} \n\
'
    return doc

@app.route('/api/search')
def search():
    query = request.args.get('query')
    resp = webscrap.getData(query)
    return dumps(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
