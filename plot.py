import pandas as pd
import plotly.express as px

tx = pd.read_csv("hs_grad_rate.csv", encoding="ISO-8859-1")
dtype = {"fips": str}

fig = px.choropleth_mapbox(tx, geojson=counties, locations='FIPS', color='hs_grad_rate',
                           color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp': 'unemployment rate'}
                           )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()