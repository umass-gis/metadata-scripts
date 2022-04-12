# Merge CSVs
This Python script merges three CSVs based on the unique ID, `mods_ID`. The script is is designed to merge the output from `1_extractXMLToCSVGetGeoNames.py` with additional metadata from the [UMass Amherst MacConnell Aerial Photo collection](https://credo.library.umass.edu/view/collection/mufs190).

## Output Fields

These are the fields which are extracted and/or calculated:

| Field        | Description                                                      | Matching field in OGM Aardvark |
|:-------------|:-----------------------------------------------------------------|:-------------------------------|
| `mods_ID`    | Unique identifier                                                | `dct_identifier_sm`            |
| `spatial`    | Place names covered by the resource (if found, otherwise 'none') | `dct_spatial_sm`               |
| `geometry`   | Extent of the resource, formatted as "ENVELOPE(W, E, N, S)"      | `locn_geometry`                |
| `bbox`       | Bounding box, also formatted as "ENVELOPE(W, E, N, S)"           | `dcat_bbox`                    |
| `place`      | Populated Place from the GeoNames database                       |                                |
| `town`       | ADM3 from the GeoNames database                                  |                                |
| `county`     | ADM2 from the GeoNames database                                  |                                |
| `state`      | ADM1 from the GeoNames database                                  |                                |
| `geoname_ID` | GeoName IDs (if found, otherwise 'none')                         | `umass_geonames_s`             |
| `titleInfo_partNumber` | Photo ID from original metadata record                 |                                |
| `place_placeTerm`      | Spatial coverage from original metadata record         |                                |
| `dateCreated`          | Creation date from original metadata record            | `dct_temporal_sm` and `dct_issued_s` |
| `year`                 | Creation year from original metadata record            | `gbl_indexYear_im`             |
| `annotation` | Note about whether or not the photo has markings                 | `umass_annotated_s`            |
