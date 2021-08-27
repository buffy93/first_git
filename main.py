#random code

from geopy.geocoders import Nominatim
from geopy import distance

def distanceCalc(von, nach):
    # API initialize
    geoloc = Nominatim(user_agent="DistanceCalcRasa")


    #Creating coordinates and the distance
    von = geoloc.geocode(von)
    nach = geoloc.geocode(nach)
    von_lat, von_lon = (von.latitude), (von.longitude)
    nach_lat, nach_lon = (nach.latitude), (nach.longitude)
    von_location = (von_lat, von_lon)
    nach_location = (nach_lat, nach_lon)
    distances = distance.distance(von_location, nach_location).km

    print(von)
    print(nach)
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print(str(round(distances, 2)))


distanceCalc("bonn", "frankfurt")
