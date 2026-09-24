# Parses a CSV with OGM Aardvark metadata into multiple JSON files.
# Designed to format the output from 3_formatCSVToAardvark.py.

# Import the required libraries
import csv
import json
import ast

# The prefix that will be used to name the output file
outputName = 'testdata'

# Define the CSV to be parsed
file = (outputName + '_3_aardvark.csv')


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
        # Retrieve the 'mods_ID' value to use in naming the output file
        mods_ID = (row['dct_identifier_sm']).removeprefix("['").removesuffix("']")

        # Format the array fields as lists
        row['dct_description_sm'] = ast.literal_eval(row['dct_description_sm'])
        row['dct_language_sm'] = ast.literal_eval(row['dct_language_sm'])
        row['dct_creator_sm'] = ast.literal_eval(row['dct_creator_sm'])
        row['dct_publisher_sm'] = ast.literal_eval(row['dct_publisher_sm'])
        row['gbl_resourceClass_sm'] = ast.literal_eval(row['gbl_resourceClass_sm'])
        row['gbl_resourceType_sm'] = ast.literal_eval(row['gbl_resourceType_sm'])
        row['dct_subject_sm'] = ast.literal_eval(row['dct_subject_sm'])
        row['dcat_theme_sm'] = ast.literal_eval(row['dcat_theme_sm'])
        row['dcat_keyword_sm'] = ast.literal_eval(row['dcat_keyword_sm'])
        row['dct_temporal_sm'] = ast.literal_eval(row['dct_temporal_sm'])
        row['gbl_indexYear_im'] = ast.literal_eval(row['gbl_indexYear_im'])
        row['dct_spatial_sm'] = ast.literal_eval(row['dct_spatial_sm'])
        row['pcdm_memberOf_sm'] = ast.literal_eval(row['pcdm_memberOf_sm'])
        row['dct_rights_sm'] = ast.literal_eval(row['dct_rights_sm'])
        row['dct_rightsHolder_sm'] = ast.literal_eval(row['dct_rightsHolder_sm'])
        row['dct_identifier_sm'] = ast.literal_eval(row['dct_identifier_sm'])

        # Format the boolean fields
        row['gbl_suppressed_b'] = makebool(row['gbl_suppressed_b'])
        row['gbl_georeferenced_b'] = makebool(row['gbl_georeferenced_b'])

        # Output individual JSON files
        out = json.dumps(row, indent=4)
        jsonoutput = open(mods_ID + '.json', 'w')
        jsonoutput.write(out)
