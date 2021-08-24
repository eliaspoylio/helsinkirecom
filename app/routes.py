from flask import render_template
from app import app

from app.recom import recom, sample

@app.route('/')
@app.route('/index')
def index():
    places = recom("3108")
    print(places['place_user_likes'])
    return render_template('index.html', place_user_likes=places['place_user_likes'], recommendations=places['recommendations'])

@app.route('/recom/places/<place_user_likes>', methods = ['GET'])
def place_recommendations(place_user_likes):
    places = recom(place_user_likes, "places")
    return places

@app.route('/recom/events/<event_user_likes>', methods = ['GET'])
def event_recommendations(event_user_likes):
    events = recom(event_user_likes, "events")
    return events

@app.route('/sample/<number>', methods = ['GET'])
def samples(number):
    places = sample(number)
    return places
