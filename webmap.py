#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip intall folium


# In[2]:


pip install folium


# In[3]:


print("pRATYUSH")


# In[4]:


pip install numpt


# In[5]:


pip install numpy


# In[8]:


import folium


# In[12]:


import folium


# In[13]:


map = folium.Map(location=[80, -100])


# In[14]:


map


# In[15]:


map.save("Map1.html")


# In[16]:


map = folium.Map([90,90])


# In[17]:


map


# In[18]:


map = folium.Map([85,23])


# In[19]:


map


# In[20]:


map.save("Map_Varanasi.html")


# In[21]:


map = folium.Map([22,84])


# In[22]:


map


# In[23]:


help(folium)


# In[24]:


help(folium.Map)


# In[29]:


map = folium.Map([88,21],zoom_start = 6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="MyMap")
fg.add_child(folium.Marker(location=[87.8,21.3],popup="Hi I am a marker",icon=folium.Icon(color="green")))
map.save("Map_example.html")


# In[26]:


dir(folium)


# In[35]:


import folium
map = folium.Map(location=[33.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
# fg.add_child(folium.Marker(location=[38.2,-99.1],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.4,-99.3],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.1,-99.6],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))

for coordinates in [[38.2,-99.1],[24.56,99.7]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Hi I am a marker!",icon=folium.Icon(color="green")))
    
    

map.add_child(fg)


# In[36]:


import pandas as pd
df = pd.read_csv("Volcanoes.txt")


# In[37]:


df


# In[39]:


type(df)


# In[40]:


df["LAT"]


# In[41]:


latitude = df["LAT"]


# In[42]:


type(latitude)


# In[45]:


len(df)


# In[46]:


type(latitude)


# In[47]:


len(latitude)


# In[48]:


latitude[0]


# In[49]:


a = [9,3,4,5,5]


# In[50]:


type(a)


# In[52]:


df.columns


# In[53]:


lat = list(latitude)


# In[54]:


lat


# In[55]:


type(lat)


# In[57]:


lon = list(df["LON"])


# In[58]:


type(lon)


# In[132]:


import folium
import pandas as pd
map = folium.Map(location=[33.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
# fg.add_child(folium.Marker(location=[38.2,-99.1],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.4,-99.3],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.1,-99.6],popup = "Hi I am a Marker", icon=folium.Icon(color='green')))
df = pd.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
el = list(df["ELEV"])
name = list(df["NAME"])
# html = """<h4>Volcano information:</h4>
# Height: %s m
# """

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for x,y,e,n in  zip(lat,lon,el,name):
    o = str(e)
    iframe = folium.IFrame(html=html % (n,n,e), width=200, height=100)
    if e > 1800:
        fg.add_child(folium.Marker(location=[x,y],popup=folium.Popup(iframe,parse_html=True),icon=folium.Icon(color="red")))
    elif e>1200 and e<=1800:
        fg.add_child(folium.Marker(location=[x,y],popup=folium.Popup(iframe,parse_html=True),icon=folium.Icon(color="orange")))
    else:
        fg.add_child(folium.Marker(location=[x,y],popup=folium.Popup(iframe,parse_html=True),icon=folium.Icon(color="blue")))
    
# fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
#                            style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x["properties"]['POP2005'] < 20000000 else 'red'}))

# fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.add_child(folium.LayerControl())
# map.save("Map_new.html")


# In[90]:


dir(folium.CircleMarker)


# In[93]:


help(folium.CircleMarker)


# In[115]:


l = lambda x: x**2
l(5)


# In[118]:


lett = lambda name: str(name) + "is chutiya"


# In[119]:


l("Pratyush")


# In[129]:


import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


# In[ ]:




