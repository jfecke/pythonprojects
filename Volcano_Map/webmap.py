import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
map = folium.Map(location=[39.82835,-98.5816684], zoom_start=5, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="TestMap")
html = """<p>Name: %s</p>
<p>Elevation: %s m</p>
<p>Status: %s</p>
"""


for i in list(range(0,len(data))):
	iframe = folium.IFrame(html=html % (data.loc[i]["NAME"], str(data.loc[i]["ELEV"]),  data.loc[i]["STATUS"]), width=200, height=120)
	fg.add_child(folium.CircleMarker(location=[data.loc[i]["LAT"], data.loc[i]["LON"]], radius=6, popup=folium.Popup(iframe), fill_color="red", color="grey", fill_opacity=0.8))

map.add_child(fg)

map.save("map1.html")


# for i in list(range(0,len(data))):
# 	print(data.loc[i]["LON"])

