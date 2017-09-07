# pip3 install googlemap

import requests
import json
import googlemaps
import datetime import datetime


def key_upload():
    gmaps = googlemaps.Client(key='AIzaSyBcgwmyrZhfVSE9m9sjGbigHpPj6TSKpZo')
    return gmaps

def get_geo_code():
    gcode_ = gmaps.geocode('5 Hannaford walk, London, UK')
    return gcode_

#[{'address_components': [{'long_name': '5', 'short_name': '5', 'types': ['street_number']}, {'long_name': 'Hannaford Walk', 'short_name': 'Hannaford Walk', 'types': ['route']}, {'long_name': 'London', 'short_name': 'London', 'types': ['postal_town']}, {'long_name': 'Greater London', 'short_name': 'Greater London', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'England', 'short_name': 'England', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United Kingdom', 'short_name': 'GB', 'types': ['country', 'political']}, {'long_name': 'E3 3TF', 'short_name': 'E3 3TF', 'types': ['postal_code']}], 'formatted_address': '5 Hannaford Walk, London E3 3TF, UK', 'geometry': {'bounds': {'northeast': {'lat': 51.5243153, 'lng': -0.0143416}, 'southwest': {'lat': 51.524162, 'lng': -0.0150972}}, 'location': {'lat': 51.5242386, 'lng': -0.0147194}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 51.5255876302915, 'lng': -0.01337041970849797}, 'southwest': {'lat': 51.5228896697085, 'lng': -0.01606838029150203}}}, 'place_id': 'ChIJqTtMdU8ddkgRscowQW-Oh6s', 'types': ['establishment', 'point_of_interest', 'premise']}]

# json_string = json.load(gcode_)


# json_string = json.dumps(gcode_)
# json_string
#'[{"address_components": [{"long_name": "5", "short_name": "5", "types": ["street_number"]}, {"long_name": "Hannaford Walk", "short_name": "Hannaford Walk", "types": ["route"]}, {"long_name": "London", "short_name": "London", "types": ["postal_town"]}, {"long_name": "Greater London", "short_name": "Greater London", "types": ["administrative_area_level_2", "political"]}, {"long_name": "England", "short_name": "England", "types": ["administrative_area_level_1", "political"]}, {"long_name": "United Kingdom", "short_name": "GB", "types": ["country", "political"]}, {"long_name": "E3 3TF", "short_name": "E3 3TF", "types": ["postal_code"]}], "formatted_address": "5 Hannaford Walk, London E3 3TF, UK", "geometry": {"bounds": {"northeast": {"lat": 51.5243153, "lng": -0.0143416}, "southwest": {"lat": 51.524162, "lng": -0.0150972}}, "location": {"lat": 51.5242386, "lng": -0.0147194}, "location_type": "ROOFTOP", "viewport": {"northeast": {"lat": 51.5255876302915, "lng": -0.01337041970849797}, "southwest": {"lat": 51.5228896697085, "lng": -0.01606838029150203}}}, "place_id": "ChIJqTtMdU8ddkgRscowQW-Oh6s", "types": ["establishment", "point_of_interest", "premise"]}]'
# json_string = json.dumps(gcode_, indent = 2)
# json_string
#'[\n  {\n    "address_components": [\n      {\n        "long_name": "5",\n        "short_name": "5",\n        "types": [\n          "street_number"\n        ]\n      },\n      {\n        "long_name": "Hannaford Walk",\n        "short_name": "Hannaford Walk",\n        "types": [\n          "route"\n        ]\n      },\n      {\n        "long_name": "London",\n        "short_name": "London",\n        "types": [\n          "postal_town"\n        ]\n      },\n      {\n        "long_name": "Greater London",\n        "short_name": "Greater London",\n        "types": [\n          "administrative_area_level_2",\n          "political"\n        ]\n      },\n      {\n        "long_name": "England",\n        "short_name": "England",\n        "types": [\n          "administrative_area_level_1",\n          "political"\n        ]\n      },\n      {\n        "long_name": "United Kingdom",\n        "short_name": "GB",\n        "types": [\n          "country",\n          "political"\n        ]\n      },\n      {\n        "long_name": "E3 3TF",\n        "short_name": "E3 3TF",\n        "types": [\n          "postal_code"\n        ]\n      }\n    ],\n    "formatted_address": "5 Hannaford Walk, London E3 3TF, UK",\n    "geometry": {\n      "bounds": {\n        "northeast": {\n          "lat": 51.5243153,\n          "lng": -0.0143416\n        },\n        "southwest": {\n          "lat": 51.524162,\n          "lng": -0.0150972\n        }\n      },\n      "location": {\n        "lat": 51.5242386,\n        "lng": -0.0147194\n      },\n      "location_type": "ROOFTOP",\n      "viewport": {\n        "northeast": {\n          "lat": 51.5255876302915,\n          "lng": -0.01337041970849797\n        },\n        "southwest": {\n          "lat": 51.5228896697085,\n          "lng": -0.01606838029150203\n        }\n      }\n    },\n    "place_id": "ChIJqTtMdU8ddkgRscowQW-Oh6s",\n    "types": [\n      "establishment",\n      "point_of_interest",\n      "premise"\n    ]\n  }\n]'
# print( json.dumps(gcode_, indent = 2))



# gcode_[0]['geometry']['location']['lat']
#51.5242386
# gcode_[0]['geometry']['location']['lat']
#51.5242386
# gcode_[0]['geometry']['location']['lng']
#-0.0147194

#####
### return the geo lat and lang for given address
#####

def get_lat_lng(address_in):
    geocode_result = gmaps.geocode(address_in)
    location_  = geocode_result[0]['geometry']['location']
    lat, lng = location_['lat'], location_['lng']
    print(lat , lng)

    return


# get_lat_lng('5 hannaford walk, london, uk')
# 51.5242386 -0.0147194




####################
#### Return the distance from A location to B location
####
####################

def get_route_instruction(address1 , address2 ):
    direction_result = gmaps.directions(address1,address2, mode='transit',departure_time = datetime.now())
    steps_ = []
    for s in direction_result[0]['legs'][0]['steps']:
        steps_.append(s['html_instructions'])
    return steps_

#   print(json.dumps(direction_result[0]['legs'][0]['steps'][0]['html_instructions']))
#   get_route_instruction('22 malting place, Reading, UK','2 Gresham Street , London, UK')

#   "Walk to Reading Station"


########################
### Return the total travel distance from given 10 location
###
################

def get_route_sum(first_ , *argv):
    prev_ = first_
#    print("First :", first_)
#    print("Second :", argv)
    sum_  = []
    sum_tot = 0
    for next_  in  argv:
        direction_result = gmaps.directions(prev_,next_, mode='transit',departure_time = datetime.now())

#        print ("Inside:", next_)
        sum_.append(direction_result[0]['legs'][0]['distance']['value'])
        sum_tot = sum_tot + direction_result[0]['legs'][0]['distance']['value']
        print("Total from => ", prev_ ,"To =>", next_," is :", direction_result[0]['legs'][0]['distance']['value'] ,"Mtr")
        prev_ = next_
    return sum_tot


