import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
map = folium.Map(location=[39.82835,-98.5816684], zoom_start=5, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="Volcano Location")
html = """<p>Name: %s</p>
<p>Elevation: %s m</p>
<p>Type: %s</p>
"""

def colorselect(vtype):
	if vtype=="Cinder cone" or vtype=="Cinder cones":
		return "orange"
	elif vtype=="Maars" or vtype=="Maar":
		return "blue"
	elif vtype=="Volcanic field":
		return "green"
	elif vtype=="Stratovolcano":
		return "red"
	else:
		return "yellow"

def population(popu):
	popu = popu["properties"]["POP2005"]
	if popu<10000000:
		return {"fillColor":"green"}
	elif popu>=10000000 and popu<20000000:
		return {"fillColor":"orange"}
	elif popu>=20000000:
		return {"fillColor":"red"}

for i in list(range(0,len(data))):
	iframe = folium.IFrame(html=html % (data.loc[i]["NAME"], str(data.loc[i]["ELEV"]), data.loc[i]["TYPE"]), width=200, height=120)
	fg.add_child(folium.CircleMarker(location=[data.loc[i]["LAT"], data.loc[i]["LON"]], radius=6, popup=folium.Popup(iframe), fill_color=colorselect(data.loc[i]["TYPE"]), color="grey", fill_opacity=0.8))

fg1= folium.FeatureGroup(name="Population")
fg1.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()), style_function=population))

map.add_child(fg1)
map.add_child(fg)
map.add_child(folium.LayerControl())


map.save("map1.html")


# for i in list(range(0,len(data))):
# 	print(data.loc[i]["LON"])

