import folium
import pandas as pd
import json

pop_data = pd.read_csv('USAcitypopulation.csv')

latitude = list(pop_data.Latitude)
longitude = list(pop_data.Longitude)
population = list(pop_data.Population)
cities = list(pop_data.AccentCity)

def population_color(pop):
    if  pop < 1000:
        return "grey"
    elif 1000 <= pop < 20000:
        return "green"
    elif 20000 <= pop < 50000:
        return "blue"
    elif 50000 <= pop < 100000:
        return "purple"
    elif 100000 <= pop < 300000:
        return "pink"
    elif 300000 <= pop < 1000000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[41.881832,-87.623177], zoom_start=8)
fg = folium.FeatureGroup(name="US Population Map")

for lt, ln, pop, c, in zip(latitude,longitude,population,cities):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str([c, pop]), radius=5,
    color = "black", fill_color = population_color(pop), fill_opacity=0.6))
map.add_child(fg)
map.save("world_citiespop.html")
