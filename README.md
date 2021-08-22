# helsinkirecom

Inspired by https://github.com/codeheroku/Introduction-to-Machine-Learning/tree/master/Building%20a%20Movie%20Recommendation%20Engine

Data is from:
http://open-api.myhelsinki.fi/

`The MyHelsinki Open API is an open interface of three databases maintained by Helsinki Marketing. It offers up-to-date information about places, events and activities in and around Helsinki for commercial purposes or the city’s development.`

## Fetch the data

`curl -X GET "http://open-api.myhelsinki.fi/v1/places/" -H  "accept: application/json" > places.json`