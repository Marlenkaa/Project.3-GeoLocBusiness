import math
import pandas as pd
from dotenv import load_dotenv
import os
from os.path import join, dirname
import requests

def coorFormat(lat,lng):
    '''Adjust coordinates format for geoqueries in MongoDB'''
    try:
        lat = float(lat)
        lng = float(lng)
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        return None

def officesClean(df):
    '''Cleans offices column and creates new column with the coordinates'''
    df = df.explode("offices")
    expand = df[["offices"]].apply(lambda r: r.offices ,result_type="expand", axis=1)
    df2 = pd.concat([df,expand],axis=1)
    df2 = df2.drop(columns=["offices"])
    df2["location"] = df2[["latitude","longitude"]].apply(lambda x:coorFormat(x.latitude,x.longitude), axis=1)
    return df2

def googleApi(place):
    '''Google API Geocode request that returns coordinates from specified space '''
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={token}").json()
    return data

def googlePlaces(place):
    '''Google API Places request that returns coordinates from specified places'''
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={address}&key={token}").json()
    return data

def cleaningPoints(point):
    '''Once we got needed data from Google API, this function gets the name and coordinates from
    each point founded and prepares the final dataframe'''
    points = []
    for i in range(len(point['results'])):
        p = {
            'name': point['results'][i]['name'],
            'latitude': point['results'][i]['geometry']['location']['lat'],
            'longitude': point['results'][i]['geometry']['location']['lng']
            }
        points.append(p)
    df_points = pd.DataFrame(points)
    df_points["location"] = df_points[["latitude","longitude"]].apply(lambda x:coorFormat(x.latitude,x.longitude), axis=1)
    return df_points