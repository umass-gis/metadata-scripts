# Reads a CSV containing basic geospatial metadata and reformats it according
# to the OGM Aardvark metadata schema. Designed to format the output from 2_mergeCSVs.py.

# Import the required libraries
import pandas as pd
from datetime import datetime

# The prefix that will be used to name the output file
outputName = 'testdata'

# Define the CSV to be formatted
file = (outputName + '_2_merged.csv')

# Retrieve the current date and time
now = datetime.now()

# Format the date and time as: YYYY-MM-DDTHH:MM:SSZ
dt_string = now.strftime('%Y-%m-%dT%H:%M:%SZ')

# Define rows and columns for the output CSV
# Columns include all Aardvark fields; fields not used by UMass are commented out
rows = []
cols = ['dct_title_s',
        # 'dct_alternative_sm',
        'dct_description_sm',
        'dct_language_sm',
        'dct_creator_sm',
        'dct_publisher_sm',
        'schema_provider_s',
        'gbl_resourceClass_sm',
        'gbl_resourceType_sm',
        'dct_subject_sm',
        'dcat_theme_sm',
        'dcat_keyword_sm',
        'dct_temporal_sm',
        'dct_issued_s',
        'gbl_indexYear_im',
        # 'gbl_dateRange_drsim',
        'dct_spatial_sm',
        'locn_geometry',
        'dcat_bbox',
        # 'dcat_centroid',
        # 'dct_relation_sm',
        'pcdm_memberOf_sm',
        # 'dct_isPartOf_sm',
        # 'dct_source_sm',
        # 'dct_isVersionOf_sm',
        # 'dct_replaces_sm',
        # 'dct_isReplacedBy_sm',
        'dct_rights_sm',
        'dct_rightsHolder_sm',
        # 'dct_license_sm',
        'dct_accessRights_s',
        'dct_format_s',
        'gbl_fileSize_s',
        # 'gbl_wxsIdentifier_s',
        'dct_references_s',
        'id',
        'dct_identifier_sm',
        'gbl_mdModified_dt',
        'gbl_mdVersion_s',
        'gbl_suppressed_b',
        'gbl_georeferenced_b',
        'umass_annotated_s',
        'umass_geonameID_s']

# Read the CSV
csv_input = pd.read_csv(file)

# Process one row at a time
for i, row in csv_input.iterrows():

    # Retrieve contents of specific fields
    mods_ID = row['mods_ID']
    geometry = row['geometry']
    bbox = row['bbox']
    geoname_ID = row['geoname_ID']
    place = row['place']
    townShort = row['town_short']
    county = row['county']
    state = row['state']
    partNumber = row['titleInfo_partNumber']
    placeTerm = row['place_placeTerm']
    dateCreated = row['dateCreated']
    year = row['year']
    annotated = row['annotation']

    # Figure out if placename is unique and format the `spatial` field
    if place == townShort:
        spatial = list([townShort + ', ' + state,
                        county + ', ' + state])
    else:
        spatial = list([place + ', ' + townShort + ', ' + state,
                        townShort + ', ' + state,
                        county + ', ' + state])

    # Read the month and day from dateCreated
    dateDT = datetime.strptime(dateCreated, "%Y-%m-%d")
    month = dateDT.strftime('%B')
    day = '{d.day}'.format(d=dateDT)

    # Append the retrieved data to the columns list
    rows.append({'dct_title_s': ('Aerial Photo of ' + townShort + ', ' + state + ' (' + partNumber + '), ' + str(year)),
                 # 'dct_alternative_sm',
                 'dct_description_sm': [
                     ('Georeferenced black-and-white aerial photograph taken on ' + month + ' ' + day + ', '
                      + str(year) + ', of ' + townShort + ' (' + county + ', ' + state
                      + '). The photograph was scanned and manually georeferenced in ArcGIS software against 2019 '
                        'color orthoimagery from the U.S. Geological Survey. Its coordinate system is NAD 1983 State '
                        'Plane Massachusetts Mainland (EPSG 26986).')
                 ],
                 'dct_language_sm': [
                     'eng'
                 ],
                 'dct_creator_sm': [
                     'MacConnell, William Preston, 1918-'
                 ],
                 'dct_publisher_sm': [
                     'University of Massachusetts at Amherst. Department of Forestry and Wildlife Management'
                 ],
                 'schema_provider_s': 'UMass',
                 'gbl_resourceClass_sm': [
                     'Imagery'
                 ],
                 'gbl_resourceType_sm': [
                     'Aerial photographs'
                 ],
                 'dct_subject_sm': [
                     'Historical aerial imagery',
                     'Black-and-white photos',
                     'Landscape'
                 ],
                 'dcat_theme_sm': [
                     'Imagery',
                     'Land Cover'
                 ],
                 'dcat_keyword_sm': [
                     'maconnell',
                     'maconell',
                     'macconnel',
                     'macconel'
                 ],
                 'dct_temporal_sm': [
                     str(year)
                 ],
                 'dct_issued_s': dateCreated,
                 'gbl_indexYear_im': [
                     year
                 ],
                 # 'gbl_dateRange_drsim': '',
                 'dct_spatial_sm': spatial,
                 'locn_geometry': geometry,
                 'dcat_bbox': bbox,
                 # 'dcat_centroid_ss': '',
                 # 'dct_relation_sm': '',
                 'pcdm_memberOf_sm': [
                     'umass-macconnell-1951'
                 ],
                 # 'dct_isPartOf_sm': '',
                 # 'dct_source_sm': '',
                 # 'dct_isVersionOf_sm': '',
                 # 'dct_replaces_sm': '',
                 # 'dct_isReplacedBy_sm': '',
                 'dct_rights_sm': [
                     'Requests to publish, redistribute, or replicate this material should be addressed to Special '
                     'Collections and University Archives, University of Massachusetts Amherst Libraries. For more '
                     'information, see http://scua.library.umass.edu/services-at-scua/permissions/. '
                 ],
                 'dct_rightsHolder_sm': [
                     'Special Collections and University Archives, University of Massachusetts Amherst Libraries'
                 ],
                 # 'dct_license_sm': '',
                 'dct_accessRights_s': 'Public',
                 'dct_format_s': 'GeoTIFF',
                 'gbl_fileSize_s': 'about 90 MB',
                 # gbl_wxsIdentifier_s': '',
                 # Multiple download links (GeoTIFF and JPG)
                 'dct_references_s': "{\"http://schema.org/url\":\"https://credo.library.umass.edu/view/full/"
                                     + mods_ID + "\",\"http://schema.org/downloadUrl\":[{"
                                                 "\"url\":\"https://credo.library.umass.edu/media/"
                                     + mods_ID + ".reference.tif\",\"label\":\"GeoTIFF\"},"
                                                 "{\"url\":\"https://credo.library.umass.edu/images/resize/full/"
                                     + mods_ID + "-001.jpg\",\"label\":\"High-Res JPG\"}],"
                                                 "\"http://iiif.io/api/image\":\"https://credo.library.umass.edu/iiif/"
                                     + mods_ID + "-001.tif/info.json\"}",
                 'id': ('umass-' + mods_ID),
                 'dct_identifier_sm': [
                     mods_ID
                 ],
                 'gbl_mdModified_dt': dt_string,
                 'gbl_mdVersion_s': 'Aardvark',
                 'gbl_suppressed_b': False,
                 'gbl_georeferenced_b': True,
                 'umass_annotated_s': annotated,
                 'umass_geonameID_s': geoname_ID
                 })

# Write the dataframe to csv
df = pd.DataFrame(rows, columns=cols)
df.to_csv(outputName + '_3_aardvark.csv', index=False)
