import rasterio as rs
from rasterio.plot import show
from rasterio.windows import Window

import georaster
import geopandas as gp

from matplotlib import pyplot as plt

from PIL import Image

import os
from os.path import dirname, abspath, join

Image.MAX_IMAGE_PIXELS = None

current_url = os.getcwd()
home_url = dirname(abspath(current_url))
data_url = os.path.join(home_url, "Data")
tiff_url = os.path.join(data_url, "GeoTiff")
other_data_url = os.path.join(data_url, "otherData")

file_name = "DHMVIIDTMRAS1m_k01.tif"
file_url = os.path.join(tiff_url, file_name)

img = Image.open(file_url)
img.show()
