# Merge CSVs
This Python script merges two CSVs based on a common field, `mods_ID`. The script is is designed to merge the output from the extractFGDCXMLToCSV.py script with additional metadata from the [UMass Amherst MacConnell Aerial Photo collection](https://credo.library.umass.edu/view/collection/mufs190). It will need to be customized before it can be used for other CSV files.

To try out the script, the `test_csv.zip` package contains 2 sample CSV files that can be merged. One is the output of the extractFGDCXMLToCSVAndGetGeoNames.py script run on the `test_XML.zip` package, and the other is the metadata about the full 1951-1952 MacConnell series.

These are the output fields:
* `mods_ID` - input to `dct_identifier_sm`
* `bbox` - input to `locn_geometry`, formatted as "ENVELOPE(W, E, N, S)"
* `geoname_ID` - input to `umass_geonames_s` (if found, otherwise 'none')
* `coverage` - input to `dct_spatial_sm` (if found, otherwise 'none')
* `titleInfo_partNumber` - input to `uri`
* `place_placeTerm` - used in calculation of `dct_title_s` and `dct_description_sm`
* `dateCreated` - input to `dct_temporal_sm` and `dct_issued_s`

## Customizations
`directoryPath` - if placed in the same folder as the XML files, this part of the code can be left as is. Otherwise, type the  path location to the folder where the XML files are stored (e.g. '/users/yourname/Desktop/xml').
