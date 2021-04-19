from flask import render_template
from app import app

from app.recomplaces import recom_random

@app.route('/')
@app.route('/index')
def index():
    places = recom_random()
    return render_template('index.html', places=places)