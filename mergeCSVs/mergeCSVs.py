# This script merges two CSVs based on a common field, “mods_ID.”  The script is is designed to merge the output from
# the extractFGDCXMLToCSV.py script with an excerpt of additional metadata about a collection of aerial photographs.
# It will need  to be customized before the script can be used for CSV files. Script based on:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# Import the required libraries
import os
import pandas as pd

# Define the working directory - update this with the location of the XML files if they are in a different folder
# than where this python script is stored
directoryPath = '.'

# Change the working directory
os.chdir(directoryPath)

# Define the two CSVs - csv1 should be the output from the extractFGDCXMLToCSV.py script
csv1 = "results.csv"
csv2 = "original_metadata.csv"

# Read the CSVs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

# Merge the CSVs
merged = df1.merge(df2, on="mods_ID", how="inner", validate="1:1").fillna("")
merged.to_csv("merged.csv", index=False)
