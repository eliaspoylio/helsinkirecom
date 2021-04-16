# helsinkirecom

Inspired by https://github.com/codeheroku/Introduction-to-Machine-Learning/tree/master/Building%20a%20Movie%20Recommendation%20Engine

## Fetch the data 

`curl -X GET "http://open-api.myhelsinki.fi/v1/places/" -H  "accept: application/json" > places.json`

## Notes

Some `places` have less tags than others so results aren't always the same I would personally give.

To use tags when finding similarities within `events` there should be some way to filter "duplicates" since many events are present as series of events. Otherwise results are just the same event on different days.