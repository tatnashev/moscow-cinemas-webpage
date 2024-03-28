

from flask import Flask, render_template, jsonify, make_response
import os


app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/cinema')
def cinema():
    return render_template ('cinema.html')

SERVICE_NAME = os.environ.get('SERVICE_NAME', 'application')


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)


