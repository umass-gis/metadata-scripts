# Merge CSVs
This Python script merges two CSVs based on a common field, `mods_ID`. The script is is designed to merge the output from `extractXMLToCSVGetGeoNames.py` with additional metadata from the [UMass Amherst MacConnell Aerial Photo collection](https://credo.library.umass.edu/view/collection/mufs190).

These are the output fields:
* `mods_ID` - input to `dct_identifier_sm`
* `bbox` - input to `locn_geometry`, formatted as "ENVELOPE(W, E, N, S)"
* `geoname_ID` - input to `umass_geonames_s` (if found, otherwise 'none')
* `coverage` - input to `dct_spatial_sm` (if found, otherwise 'none')
* `place` – used in calculations
* `town` – used in calculations
* `county` – used in calculations
* `state` – used in calculations
* `titleInfo_partNumber` - used in calculations
* `place_placeTerm` - used in calculations
* `dateCreated` - input to `dct_temporal_sm` and `dct_issued_s`
* `year` - input to `gbl_indexYear_i` and used in calculations
