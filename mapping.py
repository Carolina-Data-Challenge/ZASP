import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

tx = pd.read_csv("master_2018.csv", encoding="ISO-8859-1", dtype={"county_code": str})

fig = px.choropleth_mapbox(tx, geojson=counties, locations='county_code', color='zasp_index',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp': 'unemployment rate'}
                           )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
