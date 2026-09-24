# Metadata Scripts for UMAP GeoData
Scripts for creating geospatial metadata in the [OpenGeoMetadata Aardvark](https://opengeometadata.org) metadata schema. These records are made discoverable in the UMass Amherst Portal for Geospatial Data, or [UMAP GeoData](https://geodata.library.umass.edu/), which runs on open-source [GeoBlacklight](https://geoblacklight.org/) software.

## ScholarWorks Datasets
**These scripts can be used to make datasets in a DSpace repository discoverable in a local GeoBlacklight instance.**

[ScholarWorks](https://scholarworks.umass.edu/) is UMass Amherst's institutional repository, running on the open-source [DSpace](https://dspace.org/) software. The repository contains 100+ geospatial records with GIS-ready layers or latitude longitude coordinate data. The Python notebooks in this folder use an API to retrieve metadata from ScholarWorks to produce a human-editable spreadsheet, then convert the edited spreadsheet into individual JSON records in OGM Aardvark format. 


## SCUA Aerials
**These scripts can be used to make collections of georeferenced aerial photographs discoverable in a local GeoBlacklight instance.**

The [Robert S. Cox Special Collections and University Archives](https://scua.library.umass.edu/) at UMass Amherst Libraries is the steward of ~5,000 georeferenced black-and-white aerial photos from the [MacConnell Aerial Photo Collection](https://credo.library.umass.edu/view/collection/mufs190), dating to 1951-1952. The standalone Python scripts in this folder use bounding box coordinates to look up spatial coverage of each photo, and then produce individual JSON records in OGM Aardvark format. 
