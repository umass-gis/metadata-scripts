# This script iterates through multiple XML files generated by the "Export Metadata Multiple" tool in ArcMap,
# retrieves each item's title and bounding coordinates, retrieves the GeoNamesIDs for a given bounding box using the
# Cities and Placenames API, retrieves the upper hierarchy of the first (most important) GeoName ID, and generates a
# single CSV file with this information. The script is designed to extract relevant information about a georeferenced
# raster (aerial photo). It will need to be customized before the script can be used for other XML files.
# APIs: https://www.geonames.org/export/JSON-webservices.html#citiesJSON
# https://www.geonames.org/export/place-hierarchy.html#hierarchy
# Script based on: https://www.geeksforgeeks.org/convert-xml-to-csv-in-python/
# https://stackoverflow.com/questions/63814128/iterate-through-folders-and-find-a-file-to-put-into-a-dataframe\
# https://www.dataquest.io/blog/python-api-tutorial/
# https://stackoverflow.com/questions/16129652/accessing-json-elements

# Import the required libraries
import xml.etree.ElementTree as ET
import os
import pandas as pd
import requests
import json

"""
# Optional code to print a formatted JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
"""

# Define the working directory - update this with the location of the XML files if they are in a different folder
# than where this python script is stored
directoryPath = '.'

# Change the working directory
os.chdir(directoryPath)

# Define columns and rows for the output CSV
cols = ["mods_ID", "bbox", "geoname_ID", "coverage"]
rows = []

# Create a place to store multiple dataframes for each processed file
dfs = []

# Start the counter
record_count = 0

# Iterate through XML files in the directory
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

                # Define the parameters to be called in the GeoNames Cities and Placenames API request
                # Create a GeoNames username at http://www.geonames.org/login
                parametersCities = {
                    "north": float(northbc),
                    "south": float(southbc),
                    "east": float(eastbc),
                    "west": float(westbc),
                    "username": "demo"
                    }

                # Retrieve the Cities and Placenames information
                cities = requests.get("http://api.geonames.org/citiesJSON?", params=parametersCities)

                # Filter out just the "geonames" key
                results = cities.json()['geonames']

                # Create an empty list to store multiple GeoNamesIDs
                geonameIDs = []

                # Locate individual values for "geonameID" and append them to the list
                for i in results:
                    geonameID = i['geonameId']
                    geonameIDs.append(geonameID)

                # Proceed only if the geonameIDs list isn't empty
                if geonameIDs:

                    #Define the parameters to be called in the GeoNames Hierarchy API request
                    parametersHierarchy = {
                        "geonameId": str(geonameIDs[0]),
                        "username": "demo"
                        }

                    # Retrieve the Hierarchy information
                    hierarchy = requests.get("http://api.geonames.org/hierarchyJSON?", params=parametersHierarchy)

                    # Print the formatted JSON of this query <-- useful for testing
                    # jprint(hierarchy.json())

                    # Filter out just the "geonames" key
                    results = hierarchy.json()['geonames']

                    # Locate names of each hierarchical entity
                    for i in results:
                        if i['fcode'] == 'PPL':
                            PPL = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM3':
                            ADM3 = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM2':
                            ADM2 = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM1':
                            ADM1 = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'PCLI':
                            PCLI = i['name']
                        else:
                            pass

                    # Concat the names into a single variable
                    coverage = (PPL + ", " + ADM3 + ", " + ADM2 + ", " + ADM1 + ", " + PCLI)

                # If the geonameIDs list is empty, define the output values as "none"
                else:
                    geonameIDs.append('none')
                    coverage = "none"

                # Stage the information retrieved from this file into a temporary dataframe
                this_df = pd.DataFrame([{"mods_ID": title.removesuffix('.reference.tif'),
                                         "bbox": ("ENVELOPE(" + westbc + ", " + eastbc + ", "
                                                  + northbc + ", " + southbc + ")"),
                                         "geoname_ID": geonameIDs,
                                         "coverage": coverage
                                         }], columns=cols)

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