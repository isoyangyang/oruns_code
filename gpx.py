import gpxpy
import gpxpy.gpx
import numpy as np
import pandas as pd
import plotly.express as px
import cv2

path = '/Users/isoyang/PycharmProjects/oruns/maps/18052021.jpg'
path_gpx = '/Users/isoyang/PycharmProjects/oruns/maps/18052021.gpx'


def main():

    img = cv2.imread(path)
    dimensions = img.shape


    with open(path_gpx, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    gpx_points = gpx.tracks[0].segments[0].points

    test = gpx.get_bounds()

    df = pd.DataFrame(columns=['lon', 'lat', 'elev', 'time'])

    for point in gpx_points:
        df = df.append({'lon': point.longitude, 'lat': point.latitude, 'elev': point.elevation, 'time': point.time},
                       ignore_index=True)

    lon_min = df['lon'].loc[df['lon'].idxmin()]
    lon_max = df['lon'].loc[df['lon'].idxmax()]
    lat_min = df['lat'].loc[df['lat'].idxmin()]
    lat_max = df['lat'].loc[df['lat'].idxmax()]

    x_coordinates = []
    y_coordinates = []
    for latlon_point in gpx_points:
        x, y = map_latlon_xy(latlon_point.latitude, latlon_point.longitude, dimensions, lon_min, lon_max, lat_min, lat_max)
        x_coordinates.append(x)
        y_coordinates.append(y)

    print(df.head(10))
    print(df.min(), df.max())
    #  print(x_coordinates)
    fig_1 = px.scatter(df, x='lon', y='lat', template='plotly_dark')
    fig_1.show()

    test_array = np.column_stack((x_coordinates, y_coordinates))
    test_points = np.array(test_array)
    #  print(test_points)

    is_closed = False

    color = (255, 0, 0)
    thickness = 10

    test_image = cv2.polylines(img, np.int32([test_points]), is_closed, color, thickness)


    cv2.imshow('test', test_image)
    cv2.waitKey(0)


def map_latlon_xy(latitude, longitude, image_dimensions, lo_min, lo_max, la_min, la_max):

    map_x = ((longitude - lo_min) / (lo_max - lo_min)) * image_dimensions[0]
    map_y = ((latitude - la_min) / (la_max - la_min)) * image_dimensions[1]

    return map_x, map_y


if __name__ == '__main__':
    main()
