import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
csv_path = r'Udesh/AQI and Lat Long of Countries.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# Create a GeoDataFrame
geometry = gpd.points_from_xy(df['lng'], df['lat'])
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 24))

# 1. Plot the spatial distribution on the first subplot
gdf.plot(ax=axes[0])
axes[0].set_title('Spatial Distribution of Air Quality Index (AQI)')

# 2. Plot the hexbin on the second subplot
gdf.plot.hexbin(x='lng', y='lat', C='AQI Value', gridsize=20, cmap='YlGnBu', legend=True, ax=axes[1])
axes[1].set_title('Hexbin Plot of Air Quality Index (AQI)')

# 3. Scatter Plot of AQI Values on the third subplot
gdf.plot(kind='scatter', x='lng', y='lat', c='AQI Value', colormap='viridis', ax=axes[2])
axes[2].set_title('Scatter Plot of AQI Values')

# 4. Histogram of AQI Values on the fourth subplot
gdf['AQI Value'].plot(kind='hist', bins=30, ax=axes[3])
axes[3].set_title('Distribution of AQI Values')

# Show all plots
plt.tight_layout()  # Adjust the layout
plt.show()

# Calculate descriptive statistics for AQI values
aqi_stats = gdf['AQI Value'].describe()
print(aqi_stats)
