import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json
import csv

# with open('unemployment_rate_2019.csv', 'r') as file:
#     with open('u.csv', 'w+') as out:
#         reader = csv.DictReader(file)
#         writer = csv.writer(out)
#
#         writer.writerow(reader.fieldnames)
#
#         for row in reader:
#             writer.writerow((row['FIPS'].zfill(5), row['Unemployment_rate_2019']))

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

tx = pd.read_csv("u.csv", encoding="ISO-8859-1", dtype={"FIPS": str})
dtype = {"FIPS": str}

fig = px.choropleth_mapbox(tx, geojson=counties, locations='FIPS', color='Unemployment_rate_2019',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp': 'unemployment rate'}
                           )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
