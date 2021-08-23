import pandas as pd
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

begin = time.time()

places = pd.read_pickle("places.bin")
def get_name_fi_from_id(id):
    return places[places['id'] == id].name_fi.values[0]
def get_name_fi_from_index(index):
    return places.iloc[[index]].name_fi.values[0]
def get_tags_from_id(id):
    return places[places['id'] == id].tags.values[0]
def get_index_from_id(id):
    return places.loc[places['id'] == id].index[0]

cv = CountVectorizer() 
count_matrix = cv.fit_transform(places['tags'])
cosine_sim = cosine_similarity(count_matrix)

place_user_likes = '3108'

place_index = get_index_from_id(place_user_likes)
place_name = get_name_fi_from_id(place_user_likes)

similar_places = list(enumerate(cosine_sim[place_index]))
sorted_similar_places = sorted(similar_places,key=lambda x:x[1],reverse=True)[1:]

i=0
print('Top 5 similar places to '+place_name+' are:\n')
for element in sorted_similar_places:
    print(get_name_fi_from_index(element[0]))
    i=i+1
    if i>4:
        break

end = time.time()
print(f"Runtime: {end - begin}")