# **Data Repository Overview**

This repository is organized into multiple sections to streamline the data flow from raw input to model-ready datasets. Each section serves a distinct purpose, allowing for easy navigation and tracking of data throughout the project.

---

## **Curated Datasets**
These datasets are fully processed and ready for modeling or further analysis, reflecting the final output after preliminary processing and feature creation.

- **input_df.csv**: Contains all analyzed features after processing and feature engineering. This dataset is ready for direct use in model training.
- **input.csv**: This dataset includes all features before feature selection, with additional school-related features for location-specific modeling.

---

## **Historical Datasets**
Legacy and historical data that provide essential context for modeling and analysis, particularly around trends in rent prices, crime rates, and demand for properties.

- **count.csv**: Includes the number of properties available over time, showing demand trends in the real estate market.
- **Data_Tables_LGA_Recorded_Offences_June_2024.xlsx**: Detailed crime data by Local Government Areas (LGA) in 2021. Useful for understanding safety trends and how they may impact property prices.
- **important.csv**: Outputs from feature selection, showing the relative importance of each feature to the model's performance.
- **median.csv**: Contains the annual median rent prices, providing an overview of market trends over multiple years.

---

## **Input Datasets**
These files are split into training and testing datasets, used directly for model training, validation, and evaluation.

- **X_train.csv**: Feature set for training the model.
- **X_test.csv**: Feature set for testing and evaluating the model's performance.
- **y_train.csv**: Target variable for training.
- **y_test.csv**: Target variable for testing.

---

## **Landing Datasets**
This section contains datasets related to geographical and transportation data, as well as other contextual features like amenities. These datasets are essential for adding location-based insights to the model.

- **gtfs**: Public transportation data, offering insights into accessibility and connectivity. For more details, refer to the [GTFS documentation](https://data.ptv.vic.gov.au/downloads/GTFSReleaseNotes.pdf). 
- **OSM**: OpenStreetMap amenities data, including points of interest such as parks, hospitals, and malls. For more details, refer to the [OSM Documentation](https://wiki.openstreetmap.org/wiki/Downloading_data). 
- **SA2_2021_AUST_SHP_GDA2020**: ABS SA2 shapefiles, offering geographical boundaries used for spatial analysis. Refer to the ABS shapefile documentation for more information : [SA2 Boundary Shapefile]("https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files")
- **Victoria_DataPack**: Statistical Area 2 (SA2) data from the Australian Bureau of Statistics, providing socio-economic statistics at the SA2 level. [ABS SA2 Statistics]("https://www.abs.gov.au/census/guide-census-data/about-census-tools/community-profiles")
- **alt_properties.csv**: Scraped property data from Domain. Data is owned by Domain Group and must be used following their terms of service.
- **amenities.csv**: Amenities extracted from OpenStreetMap (OSM), such as restaurants, schools, and parks.
- **australian_postcodes.csv**: A dataset containing postcodes mapped to SA2 areas for use in geographical analysis. [Australian Postcode Documentation]("https://www.matthewproctor.com/australian_postcodes")
- **malls_melb.csv**: Locations of all shopping malls in Melbourne, extracted from the OSM database.
- **dv346-schoollocations2023.csv**: Locations of all schools in Victoria, useful for calculating proximity to educational facilities. [School location Documentation]("https://discover.data.vic.gov.au/dataset/school-locations-2023/resource/92fdd072-4666-4cc6-a28a-749c826297a7")
- **url-site**: Query file for scraping property websites, used to extract relevant property details based on keywords.

---

## **Raw Datasets**
These are the original datasets that have undergone minimal or no processing. They serve as the foundation for feature extraction and data cleaning.

- **cleaned.csv**: Cleaned version of the original scraped property data. The raw scraped data is transformed for further analysis and model building.

---

### **Notes**
- Ensure that proper licensing and permissions are followed when using scraped datasets (e.g., data from Domain or OSM).
- Further details on the transportation and geographical data can be found through the linked external documentation.

