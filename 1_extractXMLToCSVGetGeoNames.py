# Iterates through multiple FGDC XML files generated by the "Export Metadata Multiple" tool in ArcMap,
# retrieves each item's title and bounding coordinates, queries the GeoNames API to retrieve placename
# information, and appends to a single CSV file. Requires registering with GeoNames (for free) to obtain
# a username (http://www.geonames.org/login) and substituting this in the code.
#
# Converting XML to CSV: https://www.geeksforgeeks.org/convert-xml-to-csv-in-python/
# API tutorial: https://www.dataquest.io/blog/python-api-tutorial/
# Accessing JSON elements: https://stackoverflow.com/questions/16129652/accessing-json-elements

# Import the required libraries
import xml.etree.ElementTree as ET
import os
import pandas as pd
import requests
import json

# Optional code to print a formatted JSON object (useful for testing)
# def jprint(obj):
    # text = json.dumps(obj, sort_keys=True, indent=4)
    # print(text)

# Define the folder where the XML files are located
folder = 'test_data'

# Define the directory path to this folder
folderLocation = ('/users/becky/PycharmProjects/' + folder)

# Change directory
os.chdir(folderLocation)

# Define columns and rows for the output CSV
cols = ['mods_ID', 'spatial', 'geometry', 'bbox', 'place', 'town', 'county', 'state', 'geoname_ID']
rows = []

# Create a place to store multiple dataframes for each processed file
dfs = []

# Start the counter
record_count = 0

# Iterate through XML files in the directory
for file in os.listdir(folderLocation):
    if file.endswith('.xml'):

        # Increase the count each time a file is processed
        record_count = record_count + 1

        # Open an individual file and make sure to close it when done processing
        with open(file, 'r') as f:

            # Read the XML file
            tree = ET.parse(f)
            root = tree.getroot()

            # Retrieve the item's title
            for citeinfo in root.findall('./idinfo/citation/citeinfo'):
                title = citeinfo.find('title').text

            # Retrieve the item's bounding coordinates
            for bounding in root.findall('./idinfo/spdom/bounding'):
                westbc = bounding.find('westbc').text
                eastbc = bounding.find('eastbc').text
                northbc = bounding.find('northbc').text
                southbc = bounding.find('southbc').text

                # Define the parameters to be called in the GeoNames Cities and Placenames API request
                # Replace 'username' with your own username
                parametersCities = {
                    'north': float(northbc),
                    'south': float(southbc),
                    'east': float(eastbc),
                    'west': float(westbc),
                    'username': 'demo'
                    }

                # Retrieve the Cities and Placenames information
                cities = requests.get('http://api.geonames.org/citiesJSON?', params=parametersCities)

                # Print the formatted JSON of this query (useful for testing)
                # jprint(cities.json())

                # Filter out just the 'geonames' key
                results = cities.json()['geonames']

                # Create an empty list to store multiple GeoNamesIDs
                geonameIDs = []

                # Locate individual values for 'geonameID' and append them to the list
                for i in results:
                    geonameID = i['geonameId']
                    geonameIDs.append(str(geonameID))

                # Proceed only if the geonameIDs list isn't empty
                if geonameIDs:

                    # Define the parameters to be called in the GeoNames Hierarchy API request
                    # Replace 'username' with your own username
                    parametersHierarchy = {
                        'geonameId': str(geonameIDs[0]),
                        'username': 'demo'
                        }

                    # Retrieve the Hierarchy information
                    hierarchy = requests.get('http://api.geonames.org/hierarchyJSON?', params=parametersHierarchy)

                    # Print the formatted JSON of this query (useful for testing)
                    # jprint(hierarchy.json())

                    # Filter out just the 'geonames' key
                    results = hierarchy.json()['geonames']

                    # Locate names of each hierarchical entity
                    for i in results:
                        if i['fcode'] == 'PPL':
                            pplName = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM3':
                            adm3Name = i['name']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM2':
                            adm2Name = (i['name'] + ' County')
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'ADM1':
                            adm1Name = i['name']
                            adm1Code = i['adminCode1']
                        else:
                            pass

                    for i in results:
                        if i['fcode'] == 'PCLI':
                            pcliName = i['name']
                        else:
                            pass

                    # Create a list to store multiple coverage descriptions
                    spatial = list([pplName + ', ' + adm1Code,
                                    adm3Name + ', ' + adm1Code,
                                    adm2Name + ', ' + adm1Code])

                # If the geonameIDs list is empty, define the output values as 'none'
                else:
                    geonameIDs.append('')
                    pplName = ''
                    adm3Name = ''
                    adm2Name = ''
                    adm1Code = ''
                    spatial = ''

                # Stage the information retrieved from this file into a temporary dataframe
                this_df = pd.DataFrame([{'mods_ID': title.removesuffix('.reference.tif'),
                                         'spatial': spatial,
                                         'geometry': ('ENVELOPE(' + westbc + ', ' + eastbc + ', '
                                                      + northbc + ', ' + southbc + ')'),
                                         'bbox': ('ENVELOPE(' + westbc + ', ' + eastbc + ', '
                                                  + northbc + ', ' + southbc + ')'),
                                         'place': pplName,
                                         'town': adm3Name,
                                         'county': adm2Name,
                                         'state': adm1Code,
                                         'geoname_ID': geonameIDs
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
df.to_csv(folder + '_1_extract.csv', index=False)
