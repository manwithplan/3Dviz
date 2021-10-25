### Logging how to tackle the project.

You have to use the Digital Surface Map and the Digital Terrain map to build the app.
These are results of lidar surveys all around Flanders.

First step is to investigate these files.

Upon investigationg it seems that DSM shows more human built elements on the map and DTM 
shows natures levels.

From https://geodetics.com/dem-dsm-dtm-digital-elevation-models/ :

– A DEM (Digital Elevation Model) Represents the bare-Earth surface, removing all natural and built features;
– A DSM (Digital Surface Model) captures both the natural and built/artificial features of the environment, as shown below;
– A DTM (Digital Terrain Model)  typically augments a DEM, by including vector features of the natural terrain, such as rivers and ridges. A DTM may be interpolated to generate a DEM, but not vice versa.

In one of the downloaded zip files there is a pdf explaining some things.
It seems 2 main file types are to be used, 
1 : GeoTiff
2 : Shapefile

The interface will work with an addres, which will link to coordinates, which will gather information from maps.