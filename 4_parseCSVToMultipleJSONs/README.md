# Parse CSV to Multiple JSONs
This Python script reads a CSV containing [OGM Aardvark](https://opengeometadata.org) metadata and parses it into multiple JSON files. The script is designed to parse the output from `3_formatCSVToAardvark.py`.

Several of the fields need extra formatting code in order to be properly converted from CSV to JSON:
* Integer fields
* Boolean fields
* List fields

The output is a single GeoJSON file for each record. 
