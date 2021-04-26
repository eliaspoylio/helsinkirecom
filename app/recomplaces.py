import pandas as pd
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random



def recom():

    jsonData = open('places.json', 'r')
    data = json.load(jsonData)
    jsonData.close()

    places = pd.DataFrame(columns=['id', 'name_fi', 'tags'])
    count = 0
    for place in data['data']:
        itemId = place['id']
        nameFi = place['name']['fi']
        tags = ''
        for tag in place['tags']:
            tags += "'"+tag['name']+"'"
        places = places.append(
            dict(zip(places.columns, [itemId, nameFi, tags])), ignore_index=True)
        count += 1

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(places['tags'])
    cosine_sim = cosine_similarity(count_matrix)

    def get_name_fi_from_index(index):
        return places.iloc[[index]].name_fi.values[0]

    def get_index_from_id(id):
        return places[places.id == id].index[0]

    def get_tags_from_index(index):
        return places.iloc[[index]].tags.values[0]

    place_user_likes = '3108'
    place_index = get_index_from_id(place_user_likes)
    place_name = get_name_fi_from_index(place_index)
    #print(place_index)
    #print(place_name)
    #print('Tags:'+get_tags_from_index(place_index)+'\n')

    similar_places = list(enumerate(cosine_sim[place_index]))
    sorted_similar_places = sorted(
        similar_places, key=lambda x: x[1], reverse=True)[1:]

    recommendations_list = []
    recommendations_dict = {'place_user_likes':place_name}

    nr_of_recom = 4
    i = 0
    for element in sorted_similar_places:
        #print(get_name_fi_from_index(element[0]))
        recommendations_list.append(get_name_fi_from_index(element[0]))
        i = i+1
        if i > nr_of_recom:
            break
    #print (recommendations_list)

    recommendations_dict.update({'recommendations': recommendations_list})
    #print(recommendations_dict)

    return recommendations_dict
