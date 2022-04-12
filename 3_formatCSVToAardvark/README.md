# Format CSV to Aardvark
This Python script reads a CSV containing basic geospatial metadata and reformats it according to the [OGM Aardvark](https://opengeometadata.org) metadata schema. The script is designed to format the output from `2_mergeCSVs.py`.

## Customizations
`cols` - this list contains all the OGM Aardvark fields, as well as custom UMass fields. Fields you don't want can be commented out.

Reading the CSV - update this list with the column headings from your own CSV

Appending to `cols` - this list contains all the same fields as in `cols` above. Fields you don't want can be commented out. The rest will need to be updated based on your own desired outputs. For the UMass Amherst workflow, we are working with a set of historical aerial photographs that are for the most part similar; therefore we are using this part of the script to populate many fields with identical information. Alternatively, you might create a CSV with all the OGM Aardvark information, then customize this part of the script to simply read the CSV and write its contents to the fields.
