from flask import render_template
from app import app

from app.recomplaces import recom, sample

@app.route('/')
@app.route('/index')
def index():
    places = recom("3108")
    print(places['place_user_likes'])
    return render_template('index.html', place_user_likes=places['place_user_likes'], recommendations=places['recommendations'])

@app.route('/recom/<place_user_likes>', methods = ['POST', 'GET'])
def recommendations(place_user_likes):
    places = recom(place_user_likes)
    return places


@app.route('/sample/<number>', methods = ['GET'])
def samples(number):
    places = sample(number)
    return places
