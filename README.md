# BusinessGeoLoc

Este proyecto tiene como objetivo encontrar la ubicación más óptima para la apertura de nuestra nueva oficina, siendo una empresa dedicada a la industria del videojuego.

Dadas las preferencias de nuestros trabajadores, las tenidas en cuenta para este proyecto han sido:

- Proximidad a empresas dedicadas a la industria tecnológica.
- Proximidad de colegios, ya que el 30% de la plantilla tiene hijos.
- Disponibilidad de Starbucks, ya que a los ejecutivos les gusta mucho.
- Disponibilidad de aeropuerto, ya que los account manager viajan mucho.
- Disponibilidad de pubs, ya que los trabajadores tienen entre 25 y 40 años, y necesitan divertirse.

Para la obtención del lugar idóneo, se ha seguido el siguiente esquema:

1. Partiendo del dataset *companies.json*, comprobamos que la mayoría de las empresas tecnológicas se sitúan en San Francisco (*cleaning.ipynb*).
2. Obtenemos las coordenadas del aeropuerto de San Francisco mediante la Api Google Geolocation.
3. Obtenemos un dataset de Kaggle con los starbucks localizados en San Francisco.
4. Obtenemos las coordenadas de los pubs en San Francisco mediante la APi Google Places.
5. Obtenemos las coordenadas de las escuales en San Francisco mediante la Api Google Places.

Finalmente, generando queries geoespaciales en MongoDB dentro de cada una de las colecciones con los datasets, hemos obtenido que la empresa *GIS Planning* con las coordenadas *latitud: 37.784137, longitud: -122.408646* posee la mejor posición respecto a las preferencias que buscábamos. Por tanto, posicionaríamos nuestras oficinas en el mismo edificio (*analysis+geoquery.ipynb*).

En el siguiente mapa quedan representados todos los parámetros junto con la ubicación finalmente elegida:
- *En verde: Starbucks*
- *En amarillo: escuelas*
- *En rojo: pubs*

![](https://github.com/Shurlena/mongo-project/blob/master/OUTPUT/map_screenshot.png)