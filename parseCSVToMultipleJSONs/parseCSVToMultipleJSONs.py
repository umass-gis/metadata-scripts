# Parses a CSV with GeoBlacklight Aardvark metadata into multiple JSON files.
# Resources: https://fivestepguide.com/technology/machine-learning/csv-rows-to-multiple-json-python-pandas/

# Import the required libraries
import csv
import json

# Define the CSV to be parsed - should be the output from formatCSVToAardvark.py
file = 'aardvark.csv'


# Define a function to generate boolean values from strings 'True' and 'False'
def makebool(text):
    if text == 'True':
        return True
    else:
        return False


# Open the CSV and make sure to close it when done processing
with open(file, 'r') as f:

    # Read the CSV and load values into dictionary
    reader = csv.DictReader(f)

    # Process one row at a time
    for row in reader:

        # Format the integer fields
        row['gbl_indexYear_im'] = int(row['gbl_indexYear_im'])

        # Format the boolean fields
        row['gbl_suppressed_b'] = makebool(row['gbl_suppressed_b'])
        row['gbl_georeferenced_b'] = makebool(row['gbl_georeferenced_b'])

        # Clean and format the list fields: remove quotes + spaces + brackets, then split into a list
        subject1 = (row['dct_subject_sm']).replace("'", '')
        subject2 = subject1.replace(', ', ',')
        subject3 = subject2.removeprefix('[').removesuffix(']')
        row['dct_subject_sm'] = subject3.split(',')

        theme1 = (row['dcat_theme_sm']).replace("'", '')
        theme2 = theme1.replace(', ', ',')
        theme3 = theme2.removeprefix('[').removesuffix(']')
        row['dcat_theme_sm'] = theme3.split(',')

        geonames1 = (row['umass_geonames_sm']).replace("'", '')
        geonames2 = geonames1.replace(', ', ',')
        geonames3 = geonames2.removeprefix('[').removesuffix(']')
        row['umass_geonames_sm'] = geonames3.split(',')

        # Clean and format a list field with commas: remove spaces + selected quotes + brackets, then split into a list
        coverage1 = (row['dct_spatial_sm']).replace("', ", "',")
        coverage2 = coverage1.replace("['", "[").replace("']", "]").replace(",'", ",")
        coverage3 = coverage2.replace('[', '').replace(']', '')
        row['dct_spatial_sm'] = coverage3.split("',")

        # Retrieve the 'mods_ID' value to use in naming the output file
        mods_ID = row['dct_identifier_sm']

        # Output individual JSON files
        out = json.dumps(row, indent=4)
        jsonoutput = open(mods_ID + '.json', 'w')
        jsonoutput.write(out)
