import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

ax = pd.read_csv("master_2018.csv", encoding="ISO-8859-1", dtype={"county_code": str})
bx = pd.read_csv("master_2019.csv", encoding="ISO-8859-1", dtype={"county_code": str})
cx = pd.read_csv("master_linear_pred_2020.csv", encoding="ISO-8859-1", dtype={"county_code": str})
ax['Year'] = 2018
bx['Year'] = 2019
cx['Year'] = 2020
tx = pd.concat([ax, bx, cx])

fig = px.choropleth_mapbox(tx, geojson=counties, animation_frame='Year', animation_group='county_code',
                           locations='county_code', color='zasp_index',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5, range_color=[50, 100],
                           labels={'unemp': 'unemployment rate'}
                           )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
