import pandas as pd
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

begin = time.time()

events = pd.read_pickle("events.bin")
def get_name_fi_from_id(id):
    return events[events['id'] == id].name_fi.values[0]
def get_name_fi_from_index(index):
    return events.iloc[[index]].name_fi.values[0]
def get_tags_from_id(id):
    return events[events['id'] == id].tags.values[0]
def get_index_from_id(id):
    return events.loc[events['id'] == id].index[0]

cv = CountVectorizer() 
count_matrix = cv.fit_transform(events['tags'])
cosine_sim = cosine_similarity(count_matrix)

event_user_likes = 'helsinki:af3u23vhlu'

event_index = get_index_from_id(event_user_likes)
event_name = get_name_fi_from_id(event_user_likes)

similar_events = list(enumerate(cosine_sim[event_index]))
sorted_similar_events = sorted(similar_events,key=lambda x:x[1],reverse=True)[1:]

i=0
print('Top 5 similar events to '+event_name+' are:\n')
for element in sorted_similar_events:
    print(get_name_fi_from_index(element[0]))
    i=i+1
    if i>4:
        break

end = time.time()
print(f"Runtime: {end - begin}")