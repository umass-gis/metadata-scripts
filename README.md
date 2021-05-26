# Metadata Scripts
Scripts for processing metadata for GeoData, UMass Amherst's GeoBlacklight repository. All scripts are designed to work with the Aardvark metadata schema.

## extractFGDCXMLToCSV.py
Iterates through multiple XML files, extracts relevant data based on tags, and aggregates the information into a single CSV.

## extractFGDCXMLToCSVAndGetGeoNames.py
Iterates through multiple XML files, extracts relevant data based on tags, uses API queries to retrieve coverage information from the GeoNames database, and aggregates the information into a single CSV.

## mergeCSVs.py
Merges two CSVs based on a common field, `mods_ID`.
