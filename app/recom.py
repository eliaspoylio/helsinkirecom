import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

def recom(item_user_likes, category):

    items = pd.read_pickle("%s.bin" % category)
    
    def get_name_fi_from_id(id):
        return items[items['id'] == id].name_fi.values[0]
    def get_name_fi_from_index(index):
        return items.iloc[[index]].name_fi.values[0]
    def get_tags_from_id(id):
        return items[items['id'] == id].tags.values[0]
    def get_index_from_id(id):
        return items.loc[items['id'] == id].index[0]

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(items['tags'])
    cosine_sim = cosine_similarity(count_matrix)

    item_index = get_index_from_id(item_user_likes)
    item_name = get_name_fi_from_id(item_user_likes)

    similar_items = list(enumerate(cosine_sim[item_index]))
    sorted_similar_items = sorted(
        similar_items, key=lambda x: x[1], reverse=True)[1:]

    recommendations_list = []
    recommendations_dict = {'item_user_likes':item_name}

    nr_of_recom = 4
    i = 0
    for element in sorted_similar_items:
        recommendations_list.append(get_name_fi_from_index(element[0]))
        i = i+1
        if i > nr_of_recom:
            break

    recommendations_dict.update({'recommendations': recommendations_list})

    return recommendations_dict

def sample(nr):
    
    jsonData = open('places.json', 'r')
    data = json.load(jsonData)
    jsonData.close()

    places = pd.DataFrame(columns=['id', 'name_fi', 'tags'])

    for place in data['data']:
        itemId = place['id']
        nameFi = place['name']['fi']
        if (len(place['tags']) > 2):
            tags = ''
            for tag in place['tags']:
                tags += "'"+tag['name']+"'"
            places = places.append(
            dict(zip(places.columns, [itemId, nameFi, tags])), ignore_index=True)
    sample = places.sample(n=int(nr))
    return sample.to_dict('index')