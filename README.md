

## Installation

To run this script, you need to have Python installed on your system along with several libraries. Follow these steps to set up your environment:

1. **Install Python:**
   - If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/) and install it on your system.

2. **Set up a Virtual Environment (Optional but Recommended):**
   - Open your terminal or command prompt.
   - Navigate to your project directory.
   - Create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`

3. **Install Required Libraries:**
   - Ensure that `pip` is up to date:
     ```sh
     python -m pip install --upgrade pip
     ```
   - Install the required libraries:
     ```sh
     pip install geopandas pandas matplotlib
     ```

## Running the Script

- Once the installation is complete, run the script using:
  ```sh
  python geographic_analysis.py
  ```

## Diagrams Explanation

1. **Spatial Distribution Plot:**
   - This plot shows the geographical distribution of AQI data points. Each point represents the location of a measurement, providing a visual overview of the spatial spread of the data.

2. **Hexbin Plot:**
   - The hexbin plot offers a way to visualize the density of AQI data points. It is particularly useful in identifying clusters of high or low AQI values and understanding how these values are geographically distributed.

3. **Scatter Plot:**
   - This scatter plot maps AQI values against their geographical locations. Each point is colored based on its AQI value, allowing for an immediate visual understanding of the air quality at different locations.

4. **Histogram:**
   - The histogram displays the distribution of AQI values across all measured locations. It helps in understanding the frequency and spread of different AQI values, showing how common certain ranges of air quality are.

5. **Descriptive Statistics:**
   - After the plots, the script prints descriptive statistics of AQI values, including count, mean, standard deviation, minimum, quartiles, and maximum. This provides a statistical summary of the air quality data.

## Data

- Ensure that your AQI data is in a CSV format and includes 'lng' (longitude), 'lat' (latitude), and 'AQI Value' columns.
- Update the `csv_path` in the script to point to your CSV file location.
 Feel free to adjust the content according to your specific needs and data.
To use the data from the Kaggle dataset "World Air Quality Index by City and Coordinates," you need to follow these steps:

![Air Quality Index Analysis](https://github.com/ucodefusion/world-air-quality-index-by-city-and-coordinates/blob/main/Figure_1.png?raw=true)


1. **Download the Data:**
   - Visit the Kaggle dataset page: [World Air Quality Index by City and Coordinates](https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates).
   - Download the dataset to your local machine.

2. **Locate the CSV File:**
   - Unzip the downloaded file.
   - Locate the CSV file inside the unzipped folder. The name of the CSV file will depend on how the dataset author named it.

3. **Update the Script:**
   - Modify the `csv_path` in the Python script to point to the location of the downloaded CSV file. For example:
     ```python
     csv_path = r'path/to/your/downloaded/csvfile.csv'
     ```
   - Ensure that the column names in the script match those in the CSV file. The Kaggle dataset might have different column names for longitude, latitude, and AQI values. Adjust the script accordingly.

4. **Script Modifications:**
   - If the dataset has different column names, you'll need to update the script where it references `df['lng']`, `df['lat']`, and `df['AQI Value']` to match the dataset's column names.

5. **Run the Script:**
   - Follow the previously provided installation and running instructions.

6. **Data Exploration:**
   - Once the script runs successfully, it will display various plots that provide insights into the air quality index data. You can explore this data visually to understand patterns and distributions.
 
Sure, I can provide you with a README file format that includes installation instructions from the start and explanations about each diagram in the script.

---

# Geospatial Data Analysis of Air Quality Index (AQI)

This project provides a Python script for visualizing the Air Quality Index (AQI) data across various countries using geospatial analysis.
