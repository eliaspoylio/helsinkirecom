import pandas as pd
import json


def remove_duplicates(data, title):
    df = pd.DataFrame(columns=['id', 'name_fi', 'tags'])
    print('Amount of', title ,'from response metadata: ', data['meta'])
    for item in data['data']:
        itemId = item['id']
        nameFi = item['name']['fi']
        tags = ''
        for tag in item['tags']:
            tags += "'"+tag['name']+"'"
        df = df.append(
            dict(zip(df.columns, [itemId, nameFi, tags])), ignore_index=True)
    print(title, 'Length: ', len(df))

    df_duplicates_removed = df.drop_duplicates(
        subset=['name_fi'], keep='first', ignore_index=True)
    print(title, 'Length: ', len(df_duplicates_removed))

    df_duplicates_removed.to_pickle(title+'.bin')



"""
places
"""
jsonData = open('places.json', 'r')
data = json.load(jsonData)
jsonData.close()

remove_duplicates(data, "places")

"""
events
"""
jsonData = open('events.json', 'r')
data = json.load(jsonData)
jsonData.close()

remove_duplicates(data, "events")
