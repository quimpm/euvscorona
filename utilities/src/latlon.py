"""
 This module provides a high order function to make sort lists given a lat lon distance.
 Is expected from the object to use it that it has both attributes: lat and lon.
"""

import collections
import math


Point = collections.namedtuple('Point', ['lat', 'lon'])


def distance(p1: Point, p2: Point):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [p1.lon, p1.lat, p2.lon, p2.lat])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def get_lanlonkey(px: Point):
    """
        Given a point instance (lat, lon), 
        returns a function that gets the ditance to this point
    """
    return lambda x: distance(px, x)

    


