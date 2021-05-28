# This script reads a CSV containing basic metadata about a group of georeferenced aerial photos and reformats it
# according to the GeoBlacklight Aardvark metadata schema. It will need to be customized before it can be used for
# other metadata projects.

# Import the required libraries
import os
import pandas as pd
from datetime import datetime


# Change the working directory - update this with the location of the XML files if they are in a different folder
# than where this python script is stored
os.chdir('/users/becky/PycharmProjects/macconnell/results')

# Define the town <-- used in naming the output file
town = 'amherst'

# Locate the CSV to be formatted
file = (town+'_merged.csv')

# Retrieve the current date and time
now = datetime.now()

# Format the date and time as: YYYY-MM-DDTHH:MM:SSZ
dt_string = now.strftime("%Y-%m-%dT%H:%M:%SZ")

# Define row and columns for the output CSV
rows = []
cols = ["uri",
        "dct_title_s",
        # "dct_alternative_sm",
        "dct_description_sm",
        "dct_language_sm",
        "dct_creator_sm",
        "dct_publisher_sm",
        "schema_provider_s",
        "gbl_resourceClass_sm",
        "gbl_resourceType_sm",
        "dct_subject_sm",
        "dcat_theme_sm",
        # "dcat_keyword_sm",
        "dct_temporal_sm",
        "dct_issued_s",
        "gbl_indexYear_i",
        # "gbl_dateRange_drsim",
        # "umass_annotated_s",
        "umass_geonames_sm",
        "dct_spatial_sm",
        "locn_geometry",
        # "dcat_centroid_s",
        # "dct_relation_sm",
        "pcdm_memberOf_sm",
        # "dct_isPartOf_sm",
        # "dct_source_sm",
        # "dct_isVersionOf_sm",
        # "dct_replaces_sm",
        # "dct_isReplacedBy_sm",
        "dct_rights_sm",
        "dct_rightsHolder_sm",
        # "dct_license_sm",
        "dct_accessRights_s",
        "dct_format_s",
        "gbl_fileSize_s",
        # "gbl_wxsIdentifier_s",
        "dct_references_s",
        "id",
        "dct_identifier_sm",
        "gbl_mdModified_dt",
        "gbl_mdVersion_s",
        "gbl_suppressed_b",
        "gbl_georeferenced_b"]

# Read the CSV
csv_input = pd.read_csv(file)

# Process one row at a time
for i, row in csv_input.iterrows():

    # Retrieve contents of specific fields
    mods_ID = row['mods_ID']
    bbox = row['bbox']
    geoname_ID = row['geoname_ID']
    coverage = row['coverage']
    partNumber = row['titleInfo_partNumber']
    placeTerm = row['place_placeTerm']
    dateCreated = row['dateCreated']
    year = row['year']

    # Append the retrieved data to the columns list
    rows.append({"uri": partNumber,
                 "dct_title_s": ("1:20k Aerial Photograph (B/W): " + placeTerm + ", "
                                 + str(year) + " (" + partNumber + ")"),
                 "dct_alternative_sm": "",
                 "dct_description_sm": ("Georeferenced black-and-white aerial photograph captured in "
                                        + str(year) + " of " + placeTerm +
                                        ". The photograph was scanned and manually "
                                        "georeferenced in ArcMap 10.8 against 2019 color orthoimagery "
                                        "from the U.S. Geological Survey."),
                 "dct_language_sm": "English",
                 "dct_creator_sm": "MacConnell, William Preston, 1918-",
                 "dct_publisher_sm": "University of Massachusetts at Amherst. Department of Forestry and Wildlife "
                                     "Management",
                 "schema_provider_s": "UMass",
                 "gbl_resourceClass_sm": "Imagery",
                 "gbl_resourceType_sm": "Raster",
                 "dct_subject_sm": [
                     "Environment",
                     "Imagery and Base Maps",
                     "Land Cover",
                     "Planning and Cadastral",
                     "Structure"
                 ],
                 "dcat_theme_sm": [
                     "environment",
                     "imageryBaseMapsEarthCover",
                     "inlandWaters",
                     "planningCadastre",
                     "structure"
                 ],
                 "dcat_keyword_sm": "",
                 "dct_temporal_sm": dateCreated,
                 "dct_issued_s": dateCreated,
                 "gbl_indexYear_i": year,
                 "gbl_dateRange_drsim": "",
                 "umass_annotated_s": "",  # enter manually or update in workflow
                 "umass_geonames_sm": geoname_ID,
                 "dct_spatial_sm": coverage,
                 "locn_geometry": bbox,
                 "dcat_centroid_s": "",
                 "dct_relation_sm": "",
                 "pcdm_memberOf_sm": "William P. MacConnell Aerial Photograph Collection",
                 "dct_isPartOf_sm": "",
                 "dct_source_sm": "",
                 "dct_isVersionOf_sm": "",
                 "dct_replaces_sm": "",
                 "dct_isReplacedBy_sm": "",
                 "dct_rights_sm": "Requests to publish, redistribute, or replicate this material should be addressed "
                                  "to Special Collections and University Archives, University of Massachusetts Amherst "
                                  "Libraries.",
                 "dct_rightsHolder_sm": "Special Collections and University Archives, University of Massachusetts "
                                        "Amherst Libraries",
                 "dct_license_sm": "",
                 "dct_accessRights_s": "Public",
                 "dct_format_s": "GeoTIFF",
                 "gbl_fileSize_s": "90 MB",
                 "gbl_wxsIdentifier_s": "",
                 "dct_references_s": "{\"http://schema.org/url\":\"https://credo.library.umass.edu/view/full/"
                                     + mods_ID + "\",\"http://schema.org/downloadUrl\":\"https://credo.library.umass.edu/media/"
                                     + mods_ID + ".reference.tif\",\"http://iiif.io/api/image\":\"https://credo.library.umass.edu/iiif/"
                                     + mods_ID + "-001.tif/info.json\"}",
                 "id": ("umass-"+mods_ID),
                 "dct_identifier_sm": mods_ID,
                 "gbl_mdModified_dt": dt_string,
                 "gbl_mdVersion_s": "Aardvark",
                 "gbl_suppressed_b": False,
                 "gbl_georeferenced_b": True
                 })

# Write the dataframe to csv
df = pd.DataFrame(rows, columns=cols)
df.to_csv(town+'_aardvark.csv', index=False)
