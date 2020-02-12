import math
import pandas as pd

def coorFormat(lat,lng):
    '''Ajusta el formato de las coordenadas para las geoqueries'''
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
    '''Limpia la columna offices y crea nueva columna con las coordenadas'''
    df = df.explode("offices")
    expand = df[["offices"]].apply(lambda r: r.offices ,result_type="expand", axis=1)
    df2 = pd.concat([df,expand],axis=1)
    df2 = df2.drop(columns=["offices"])
    df2["location"] = df2[["latitude","longitude"]].apply(lambda x:coorFormat(x.latitude,x.longitude), axis=1)
    return df2