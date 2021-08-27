# Merges three CSVs based on a common field, 'mods_ID.'  Designed to merge the output from
# extractXMLToCSVGetGeoNames.py with CSVs containing additional metadata.
# Script based on: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# Import the required libraries
import pandas as pd

# Define the two CSVs
# csv1 should be the output from extractXMLToCSVGetGeoNames.py
# csv2 and csv3 should contain additional metadata
csv1 = 'extract.csv'
csv2 = 'scua.csv'
csv3 = 'annotation.csv'

# Read the CSVs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
df3 = pd.read_csv(csv3)

# Merge the CSVs
merged = df1.merge(df2, on='mods_ID', how='inner', validate='1:1')\
    .merge(df3, on='mods_ID', how='inner', validate='1:1').fillna('')
merged.to_csv(town + '_merged.csv', index=False)
