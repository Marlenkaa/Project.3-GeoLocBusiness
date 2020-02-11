import math
import requests
from geopandas import GeoDataFrame
from shapely.geometry import Point
import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Ajusta el formato de las coordenadas.
def coorFormat(lat,lng):
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

# Limpia la columna offices y crea nueva columna con las coordenadas.
def officesClean(df):
    df = df.explode("offices")
    expand = df[["offices"]].apply(lambda r: r.offices ,result_type="expand", axis=1)
    df2 = pd.concat([df,expand],axis=1)
    df2 = df2.drop(columns=["offices"])
    df2["location"] = df2[["latitude","longitude"]].apply(lambda x:coorFormat(x.latitude,x.longitude), axis=1)
    return df2

# API a geocode que devuelve las coordenadas de una dirección.
def getLocation(address):
    
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }

# Completa las coordenadas que están en blanco pero tienen dirección1 -- NO FUNCIONA
def fillCoord(df,col):
    col_nulls = df[col].isnull()
    null_df = df[col_nulls]
    idx = null_df.index
    for i in range(len(idx)):
        if df.address1[idx[i]] != None and df.address1[idx[i]] != '':
            df.set_value(idx[i],col,getLocation(df.address1[idx[i]]))
    return df

# Completa las coordenadas que están en blanco pero tienen dirección2 -- NO FUNCIONA
def fillCoord2(df,col):
    col_nulls = df[col].isnull()
    null_df = df[col_nulls]
    idx = null_df.index
    for i in range(len(idx)):
        if df.address2[idx[i]] != None and df.address2[idx[i]] != '':
            df.set_value(idx[i],col,getLocation(df.address2[idx[i]]))
    return df

# Devuelve formato query para aplicar sobre dataset en MongoDB y filtrar por distancia desde un punto.
def queryDist(location,maxDistance=2000,minDistance=0,field="location"):
    return {
       field: {
         "$near": {
           "$geometry": location if type(location)==dict else getLocation(location),
           "$maxDistance": maxDistance,
           "$minDistance": minDistance
         }
       }
    }

# Devueñve las coordenadas de un sitio
def googleApi(place):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={token}").json()
    return data

# Devuelve los lugares solicitados con sus coordenadas
def googlePlaces(place):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={address}&key={token}").json()
    return data
