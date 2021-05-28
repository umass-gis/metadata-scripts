# Metadata Scripts
Scripts for processing metadata for GeoData, UMass Amherst's GeoBlacklight repository. The workflow transforms basic metadata about a collection of georeferenced aerial photos in the [UMass Amherst MacConnell Aerial Photo collection](https://credo.library.umass.edu/view/collection/mufs190) so that the photos can be made discoverable in [GeoBlacklight](https://geoblacklight.org) applications.

To try out the scripts, the `test_data.zip` package contains 16 sample XML files of georeferenced aerial photos of the town of Amherst, MA, the file `scua.csv` with additional metadata about the full aerial photo collection, and outputs from each of the scripts.

## Step 1: extractXMLToCSVGetGeoNames.py
Iterates through multiple XML files containing bounding coordinates, extracts relevant data based on tags, uses API queries to retrieve coverage information from the GeoNames database, and aggregates the information into a single CSV.

## Step 2: mergeCSVs.py
Merges the output from Step 1 with another CSV containing additional metadata. The merge is done on a common field, `mods_ID`.

## Step 3: formatCSVtoAardvark.py
Formats the output from Step 2 into the GeoBlacklight Aardvark metadata schema.

## Step 4: parseCSVToMultipleJSONs.py
Parses the output from Step 3 into multiple JSON files (one per item) that can be ingested into GeoBlacklight applications. 
