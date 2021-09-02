#random code
# giving distance between 2 places

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

    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print(str(round(distances, 2)))
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")

def Cityname (von, nach):
    # API initialize
    geoloc = Nominatim(user_agent="DistanceCalcRasa")

    von = geoloc.geocode(von)
    nach = geoloc.geocode(nach)

    print("First City : " + von)
    print("-------------------------------------------------------------------------------")
    print("Secound City : " + nach)


distanceCalc("bonn", "frankfurt")
