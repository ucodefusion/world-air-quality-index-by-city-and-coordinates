import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
csv_path = r'Data/AQI and Lat Long of Countries.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# Create a GeoDataFrame
geometry = gpd.points_from_xy(df['lng'], df['lat'])
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Plot the spatial distribution
gdf.plot()
plt.title('Spatial Distribution of Air Quality Index (AQI)')
plt.show()

# Choropleth-Like Hexbin plot to visualize AQI values
gdf.plot.hexbin(x='lng', y='lat', C='AQI Value', gridsize=20, cmap='YlGnBu', legend=True)
plt.title('Hexbin Plot of Air Quality Index (AQI)')
plt.show()

# Calculate descriptive statistics for AQI values
aqi_stats = gdf['AQI Value'].describe()
print(aqi_stats)
