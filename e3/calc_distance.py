import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pykalman import KalmanFilter
from xml.dom.minidom import parse, parseString
from math import cos, asin, sqrt, pi

filename = sys.argv[1]

def to_data(elem):
    latitude = float(elem.getAttribute("lat"))
    lontitude = float(elem.getAttribute("lon"))
    return latitude, lontitude

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Adapted from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
    answered by user Salvador Dali
    """
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))* 1000  # unit in meters



def pre_process(data):
    data['shift_lat'] = data['lat'].shift(periods=1)
    data['shift_lon'] = data['lon'].shift(periods=1)
    return data


def distance(data):
    data = pre_process(data)
    data['sum'] = data.apply(lambda row: calculate_distance(row['lat'], row['lon'], row['shift_lat'], row['shift_lon']),axis = 1 )
    sum = data['sum'].sum()
    return sum


def output_gpx(points, output_filename):
    """
    Adapted from calc_distance_hint.py
    Output a GPX file with latitude and longitude from the points DataFrame.

    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)

    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)

    points.apply(append_trkpt, axis=1, trkseg=trkseg, doc=doc)

    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')


"""
points = pd.DataFrame({
    'lat': [49.280158, 49.280222, 49.280231],
    'lon': [123.005283, -123.005437, -123.005601]})

print(round(distance(49.280158,-123.005283,49.280222,-123.005437),6))
"""


walk_doc = parse(filename)
walk_element = walk_doc.getElementsByTagName('trkpt')
points  = pd.DataFrame(list(map(to_data,walk_element)), columns = ['lat', 'lon'])
#print(points)
print('Unfiltered distance: %0.2f' % (distance(points)))

############################################
kalman_data = points[['lat', 'lon']]
initial_state = kalman_data.iloc[0]
#print(initial_state)
o_covariance = np.diag([0.00015,0.00015]) ** 2 # TODO: shouldn't be zero
t_covariance = np.diag([0.00005,0.00005]) ** 2 # TODO: shouldn't be zero
transition = [[1, 0], [0, 1]]
kf = KalmanFilter(initial_state_mean = initial_state,
                    initial_state_covariance = o_covariance,
                    observation_covariance = o_covariance,
                    transition_covariance = t_covariance,
                    transition_matrices = transition )
kalman_smoothed, _ = kf.smooth(kalman_data)
#print(kalman_smoothed)
filtered_walk = pd.DataFrame(kalman_smoothed, columns =['lat', 'lon'])


print('filtered distance: %0.2f' % (distance(filtered_walk)))
output_gpx(filtered_walk, 'out.gpx')
#print(walk_data)
