from dotenv import load_dotenv
import os
from os.path import join, dirname
import requests

def googleApi(place):
    '''Devuelve las coordenadas de un lugar indicado'''
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={token}").json()
    return data

def googlePlaces(place):
    '''Devuelve los lugares solicitados con sus coordenadas'''
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("TOKEN")
    address = place
    data = requests.get(f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={address}&key={token}").json()
    return data