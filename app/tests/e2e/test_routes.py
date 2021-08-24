import requests

"""
Place and events ids may not work in the future!
"""
def test_get_place_recommendations__check_status_code_equals_200():
     response = requests.get("http://localhost:5000/recom/places/3108")
     assert response.status_code == 200

def test_get_event_recommendations__check_status_code_equals_200():
     response = requests.get("http://localhost:5000/recom/events/helsinki:af3u23vhlu")
     assert response.status_code == 200