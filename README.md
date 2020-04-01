# *GeoLocBusiness*

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.3-GeoLocBusiness/master/images/front.jpg" width="400">
</p>

The goal of this project is to find the best location to place new company offices. Given a company that belongs to the gaming industry, the location elected must to comply the following preferences:

- Proximity to other tech companies.
- Proximity to schools, as the 30% of employees has children.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot, there must be an airpoirt.
- All people in the company have between 25 and 40 years, give them some place to go to party.

### INPUT

We start from a json file with a bunch of companies which we will use to choose the city where we are going to concentrate our search.

Once the city is elected, we got a csv file with all starbucks located in that area from Github: https://gist.github.com/dankohn/09e5446feb4a8faea24f#file-starbucks_us_locations-csv

### OUTPUT

Here we can find all datasets that were cleaned and prepared to be introduced in MongoDB and able to execute geoqueries.

Furthermore, the final map result with all coordinates and final decision is saved here as *best_location_map.html*

### src

* *dataPrep.py* -> functions that clean parts of datasets, adjut coordinates for MongoDB geoqueries or conect with Google API.

* *geoquery.py* -> functions that execute geoqueries in MongoDB.

* *dataPrep.ipynb* -> makes all the cleaning process, gets necessary data from Google API and prepare the datasets for next steps. Also, here we make our first decision to focus our search in San Francisco (EE.UU), as there is the mayority concentration of tech companies.

### finalDecision.ipynb

Once we have all coordinates ready from all the places that videogame company requested, we start to display them in a map of San Francisco city. The last step is to decide where the new offices will be open. For that purpose, we determined that we will compare the distance from each of the tech companies to the different required places, in order to get the company that satisfies the proximity to all of them (1,5km at most).

For that, we execute geoqueries that return how many matches each company satisfies and score them according to the importance we decided to give them. In this case:

- Starbucks proximity match will score with 0.5
- Pubs proximity match will score with 0.35
- Schools proximity match will score with 0.15
- If a company has at least one match in every three requirements, the final score will be duplicated

This scoring method returns us 'PX Interactive' as winner company with the best location of San Francisco. Here we can see the hole map with every place located and marked:

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.3-GeoLocBusiness/master/images/complete_map.png" width="600">
</p>

If we zoom it, we can check the 1,5km radio where the new offices could be open. For further info:

- *PX Interactive coordinates: 37.781754, -122.407709*
- *Starbucks marked in green*
- *Pubs marked in red*
- *Schools marked in yellow*
- *Airport marked in blue (see complete map)*
- *Tech companies represented in heat map*

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.3-GeoLocBusiness/master/images/best_location.png" width="600">
</p>