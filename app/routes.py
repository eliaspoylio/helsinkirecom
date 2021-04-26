from flask import render_template
from app import app

from app.recomplaces import recom

@app.route('/')
@app.route('/index')
def index():
    places = recom()
    print(places['place_user_likes'])
    return render_template('index.html', place_user_likes=places['place_user_likes'], recommendations=places['recommendations'])