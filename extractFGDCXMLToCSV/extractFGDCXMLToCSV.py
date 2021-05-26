# This script iterates through multiple XML files generated by the "Export Metadata Multiple" tool in ArcMap,
# retrieves each item's title and bounding coordinates, and generates a single CSV file with this information. The
# script is designed to extract relevant information about a georeferenced raster (aerial photo), and so it will need
# to be customized before the script can be used for other XML files. Script based on
# https://www.geeksforgeeks.org/convert-xml-to-csv-in-python/ with help from
# https://stackoverflow.com/questions/63814128/iterate-through-folders-and-find-a-file-to-put-into-a-dataframe

# Import the required libraries
import xml.etree.ElementTree as ET
import os
import pandas as pd

# Define the working directory - update this with the location of the XML files if they are in a different folder
# than where this python script is stored
directoryPath = '.'

# Change the working directory
os.chdir(directoryPath)

# Define columns and rows for the output CSV
cols = ["mods_ID", "bbox"]
rows = []

# Create a place to store multiple dataframes for each processed file
dfs = []

# Start the counter
record_count = 0

# Iterate through files in the directory
for file in os.listdir(directoryPath):
    if file.endswith(".xml"):

        # Increase the count each time a file is processed
        record_count = record_count + 1

        # Open an individual file and make sure to close it when done processing
        with open(file, 'r') as f:

            # Read the XML file
            tree = ET.parse(f)
            root = tree.getroot()

            # Retrieve the item's title
            for citeinfo in root.findall("./idinfo/citation/citeinfo"):
                title = citeinfo.find("title").text

            # Retrieve the item's bounding coordinates
            for bounding in root.findall("./idinfo/spdom/bounding"):
                westbc = bounding.find("westbc").text
                eastbc = bounding.find("eastbc").text
                northbc = bounding.find("northbc").text
                southbc = bounding.find("southbc").text

                # Stage the information retrieved from this file into a temporary dataframe
                this_df = pd.DataFrame([{"mods_ID": title.removesuffix('.reference.tif'),
                                         "bbox": ("ENVELOPE(" + westbc + ", " + eastbc + ", "
                                                  + northbc + ", " + southbc + ")")}], columns=cols)

            # Append this dataframe to the dfs list
            dfs.append(this_df)

    # Do nothing if the file ends with anything other than .xml
    else:
        pass

# Print the number of records processed
print(record_count)

# Concatenate all the dfs into a single dataframe
df = pd.concat(dfs)

# Write the dataframe to csv
df.to_csv('results.csv', index=False)
