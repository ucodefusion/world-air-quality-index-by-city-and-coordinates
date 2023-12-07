To use the data from the Kaggle dataset "World Air Quality Index by City and Coordinates," you need to follow these steps:

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
 