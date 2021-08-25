from flask import Flask, request, render_template, jsonify
from app import app

from app.recom import recom, sample, available


@app.route('/')
@app.route('/index')
def index():
    places_available = available("places")
    places = recom("3108", "places")
    return render_template('index.html',
                           places_available=places_available,
                           place_user_likes=places['item_user_likes'],
                           recommendations=places['recommendations'])

@app.route("/search/<string:box>")
def process(box):
    query = request.args.get('query')
    places_available = available("places")
    if box == 'places':
        filtered = [place for place in places_available if place['value'].startswith(query)]
        suggestions = filtered
    return jsonify({"suggestions":suggestions})


@app.route('/recom/places/<place_user_likes>', methods=['GET'])
def place_recommendations(place_user_likes):
    places = recom(place_user_likes, "places")
    return places


@app.route('/recom/events/<event_user_likes>', methods=['GET'])
def event_recommendations(event_user_likes):
    events = recom(event_user_likes, "events")
    return events


@app.route('/sample/<number>', methods=['GET'])
def samples(number):
    places = sample(number)
    return places
