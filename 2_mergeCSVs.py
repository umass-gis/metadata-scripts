# Merges three CSVs based on the unique ID, 'mods_ID.' Designed to merge the output from
# 1_extractXMLToCSVGetGeoNames.py with CSVs containing additional metadata.

# Import the required libraries
import pandas as pd

# The prefix that will be used to name the output file
outputName = 'testdata'

# Define the CSVs
# csv1 should be the output from 1_extractXMLToCSVGetGeoNames.py
# csv2 and csv3 should contain additional metadata
csv1 = (outputName + '_1_extract.csv')
csv2 = './helper_docs/scua.csv'
csv3 = './helper_docs/annotation.csv'

# Read the CSVs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
df3 = pd.read_csv(csv3)

# Merge the CSVs
merged = df1.merge(df2, on='mods_ID', how='left', sort=True, validate='1:1')\
    .merge(df3, on='mods_ID', how='left', validate='1:1').fillna('')
merged.to_csv(outputName + '_2_merged.csv', index=False)
