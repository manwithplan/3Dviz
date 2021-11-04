# 3Dviz

The goal of this project is to create 3-dimensional visualations for a given address somewhere in Flanders.

<img src="gerechtsgebouw.jpg" alt="Justitiepaleis" width="200"/>
<img src="chrome_Dj0hEWoBfS.jpg" alt="Visualisatie" width="200"/>

### Structure

Project is divided into 2 folders:

- **Code**: containing a jupyter notebook containing the functional code
- **Data**: containing GeoTiff files of DTM and DSM data.

### Tech

The source code uses the folowing libraries:
- **rasterio** for handling the tiff files
- **matplotlib** for handling al the plotting functionality
- **os** for navigating local folders on the system
- **numpy** for all numerical array calculations of the tiff files
- **requests** handling communication with the api's
- **json** for formatting those communcations

### Roadmap

The basic demands of the project have been met.
Further experimentation with API's such as the QGIS and GeoServer are to be implemented.

### Installation

- Clone the repository / download the files. Open your terminal and navigate to this directory.
- Open the notebook, execute all the cells and fill out the address you want visualized in the last cell.
- Watch the magic happen

### Limitations

Because of the large size only a few GeoTiff files have been downloaded. If the requested address is out of bounds
the program will specify which .tiff file should be downloaded and placed in the correct Data Folder.

### Data

The .tiff files come from the following websites:
- [Detailed Surface Model](https://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
- [Detailed Terrain Model](https://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)

