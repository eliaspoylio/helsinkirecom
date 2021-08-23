import pandas as pd
import requests


def get_data(category):
    """
    Get data from myhelsinki API
    """
    url = "http://open-api.myhelsinki.fi/v1/%s/" % category
    data = requests.get(url)
    return data.json()

def remove_duplicates(data, title):
    """
    Create a dataframe from JSON data.
    Remove duplicates (by name) and save the data in serialised form.
    """
    df = pd.DataFrame(columns=['id', 'name_fi', 'tags'])
    print("Amount of", title ,"from response metadata: ", data['meta'])
    for item in data['data']:
        itemId = item['id']
        nameFi = item['name']['fi']
        tags = ''
        for tag in item['tags']:
            tags += "'"+tag['name']+"'"
        df = df.append(
            dict(zip(df.columns, [itemId, nameFi, tags])), ignore_index=True)
    print(title, "Length: ", len(df))

    df_duplicates_removed = df.drop_duplicates(
        subset=['name_fi'], keep="first", ignore_index=True)
    print(title, "Length: ", len(df_duplicates_removed))

    df_duplicates_removed.to_pickle(title+".bin")



"""
places
"""
data = get_data("places")
remove_duplicates(data, "places")

"""
events
"""
data = get_data("events")
remove_duplicates(data, "events")
