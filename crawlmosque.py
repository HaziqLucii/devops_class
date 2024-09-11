import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# API URL
lat = 5.056870
lon = 108.554843
distance = 70000000
api_url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/nearestMosque&lat='+ str(lat) +'&long=' + str(lon) + '&dist=' + str(distance)

# Fetch data from the API
response = requests.get(api_url)
data = response.json()

# Extract location data
location_data = data['locationData']

# Convert the location data to a DataFrame
df = pd.DataFrame(location_data)

# Function to safely convert to float
def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        return None  # Return None or a default value if conversion fails

# Apply the function to convert latitude and longitude
df['latitud'] = df['latitud'].apply(safe_float_conversion)
df['longitud'] = df['longitud'].apply(safe_float_conversion)

# Drop rows where conversion failed (latitude or longitude is None)
df = df.dropna(subset=['latitud', 'longitud'])

# Convert latitude and longitude to a geometry column
df['geometry'] = df.apply(lambda row: Point(row['longitud'], row['latitud']), axis=1)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Set the coordinate reference system (CRS), if known
gdf.set_crs(epsg=4326, inplace=True)  # WGS84

# Optionally, save the GeoDataFrame to a file (e.g., GeoJSON)
gdf.to_file('mosque.geojson', driver='GeoJSON')

# Export the GeoDataFrame to a shapefile
gdf.to_file('mosque.shp', driver='ESRI Shapefile')

# Print the GeoDataFrame
print(gdf)