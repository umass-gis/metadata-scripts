# Merges two CSVs based on a common field, 'mods_ID.'  Designed to merge the output from
# extractXMLToCSVGetGeoNames.py with another CSV containing additional metadata.
# Script based on: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# Import the required libraries
import pandas as pd

# Define the two CSVs
# csv1 should be the output from extractXMLToCSVGetGeoNames.py
# csv2 should be the file containing additional metadata
csv1 = 'extract.csv'
csv2 = 'scua.csv'

# Read the CSVs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

# Merge the CSVs
merged = df1.merge(df2, on='mods_ID', how='inner', validate='1:1').fillna('')
merged.to_csv('merged.csv', index=False)
