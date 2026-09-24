# Validates a JSON file against the OGM Aardvark JSON schema.
# Designed to validate the output from parseCSVToMultipleJSONs.py.

# Import the required libraries
import json
import jsonschema
from jsonschema import validate
import os

# Define the JSON schema file
with open('./helper_docs/geoblacklight-schema-aardvark.json', 'r') as s:
    aardvarkSchema = json.load(s)

# Start the counter
record_count = 0

# Create a variable to store error messages
error = None

# Iterate through JSON files in the directory
for file in os.listdir('.'):
    if file.endswith('.json'):
        # Increase the count each time a file is processed
        record_count = record_count + 1

        # Open an individual file and make sure to close it when done processing
        with open(file, 'r') as f:
            # Read the JSON file
            geoJSON = json.load(f)

            # Validate the JSON file
            try:
                validate(instance=geoJSON, schema=aardvarkSchema)
            except jsonschema.exceptions.ValidationError as err:
                print("Error identified in", file, ":")
                print(err)
                error = err

if error is not None:
    print("WARNING: There is an error in one or more of the records. See above for details.")
else:
    print("All ", record_count, " records are valid.")
