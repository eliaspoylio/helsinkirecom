from flask import Flask, request, render_template, jsonify
from app import app

from app.recom import recom, sample, available


@app.route('/')
@app.route('/index')
def index():
    places_available = available("places")
    return render_template('index.html',
                           places_available=places_available,
                           )


@app.route("/search/<string:box>")
def process(box):
    query = request.args.get('query')
    places_available = available("places")
    if box == 'places':
        filtered = [
            place for place in places_available if place['value'].startswith(query)]
        suggestions = filtered
    return jsonify({"suggestions": suggestions})


@app.route('/response', methods=['POST'])
def response():
    place = request.form.get("place")
    print(place)
    places_available = available("places")
    place_id = next(item['data'] for item in places_available if item['value'] == place)
    print(place_id)
    places = recom(place_id, "places")
    return render_template("index.html",
                           place_user_likes=places['item_user_likes'],
                           recommendations=places['recommendations'])


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
