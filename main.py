## Automatically get data from USGS.gov on earthquakes over 4.5 magnitude in the last 30 days

import requests
import plotly.express as px

def show_earthquakes():
    """Pulls data from USGS.gov and charts using plotly.express"""
    # Static URL for automated feed
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
    response = requests.get(url)

    # Check status codes
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Convert to JSON
    all_eq_data = response.json()

    # Extract features dictionary
    all_eq_dicts = all_eq_data['features']

    # Define empty lists
    mags, lons, lats = [], [], []

    # Extract data
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

    # Visualize the data
    title = "USGS Magnitude 4.5+ Earthquakes, Past Month"
    
    # Custom color scale
    custom_color_scale = [
        [0, "#ffcc00"],  # Bright yellow
        [0.25, "#66ff66"],  # Lime green
        [0.5, "#0099ff"],  # Sky blue
        [0.75, "#ff66ff"],  # Hot pink
        [1, "#ff0000"],  # Bright red
    ]

    fig = px.scatter_geo(
        lat=lats,
        lon=lons, 
        title=title,
        color=mags,
        color_continuous_scale=custom_color_scale,
        labels={'color':'Magnitude'},
        projection='natural earth',
    )

    fig.show()

show_earthquakes()