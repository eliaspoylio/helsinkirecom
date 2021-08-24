import requests
import re

"""
Place and events ids may not work in the future!
"""
def test_get_place_recommendations_with_value_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/recom/places/3108")
     assert response.status_code == 200

def test_get_event_recommendations_with_value_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/recom/events/helsinki:af3u23vhlu")
     assert response.status_code == 200

"""
test index
"""
def test_get_index_check_status_code_equals_200():
     response = requests.get("http://localhost:5000/")
     assert response.status_code == 200

def test_get_index_check_body_matches_regex():
     response = requests.get("http://localhost:5000/")
     response_body = response.text
     assert re.search("Recommendations", response_body)