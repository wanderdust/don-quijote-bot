from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import request
import os
from bot import start_text
import json

# Start app
# Change default location of index.html from ./templates to ./static
app = Flask(__name__,
    static_url_path='',
    template_folder='static')

# Activate CORS.
CORS(app, resources={r'/*': {'origins': 'http://localhost:5000'}})

# Global variables
publicPath = '{}/'.format(os.getcwd())

@app.route("/api/predict/", methods = ['GET', 'POST'])
def root():
    init_text = request.data.decode("utf-8")
    init_text = json.loads(init_text)

    text = start_text(init_text['text'])

    return jsonify({'text': text})



if __name__ == '__main__':
  app.run() 


"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""