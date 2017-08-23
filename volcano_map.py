import folium
import pandas as pd
import json

vdata = pd.read_csv("Volcanoes.txt")
lat = list(vdata.LAT)
lon = list(vdata.LON)
elevation = list(vdata.ELEV)
names = list(vdata.NAME)
locations = list(vdata.LOCATION)

def elvation_color(elev):
    if elev < 2000:
        return "green"
    elif 2000 <= elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[40.7608, -111.8910], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="my map")

for lt, ln, n, el, l in zip(lat, lon, names, elevation, locations):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str([n, el, l]), radius=8,
    color = "black", fill_color = elvation_color(el), fill_opacity=0.6))


map.add_child(fg)
map.save("Volcano_map.html")
