# Merges three CSVs based on the unique ID, 'mods_ID.' Designed to merge the output from
# 1_extractXMLToCSVGetGeoNames.py with CSVs containing additional metadata.
#
# Script based on: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# Import the required libraries
import os
import pandas as pd

# Define the folder where the output from Step 1 is located
folder = 'test_data'

# Define the directory path to this folder, change directory
os.chdir('/users/becky/PycharmProjects/' + folder)

# If additional CSVs are stored somewhere else, define that location;
# if stored with the output from Step 1, keep the structure of this code:
# csvLocation = ('/users/becky/PycharmProjects/' + folder + '/')
csvLocation = ('/users/becky/PycharmProjects/' + folder + '/')

# Define the CSVs
# csv1 should be the output from 1_extractXMLToCSVGetGeoNames.py
# csv2 and csv3 should contain additional metadata
csv1 = (folder + '_1_extract.csv')
csv2 = (csvLocation + 'scua.csv')
csv3 = (csvLocation + 'annotation.csv')

# Read the CSVs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
df3 = pd.read_csv(csv3)

# Merge the CSVs
merged = df1.merge(df2, on='mods_ID', how='inner', validate='1:1')\
    .merge(df3, on='mods_ID', how='inner', validate='1:1').fillna('')
merged.to_csv(folder + '_2_merged.csv', index=False)
