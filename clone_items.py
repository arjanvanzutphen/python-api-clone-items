#######
#
# Esri GIS Tech 2018
# Python Clone_items Example
#
# Author: AVZ
# Esri Nederland (c) 2018
#
import arcgis
from arcgis import *
import config

gis = arcgis.GIS("http://arcgis.com", config.username, config.password)
print("Connected to arcgis.com")

# Create contentManager object for manipulating ArcGIS Content
contentManager = arcgis.gis.ContentManager(gis)
print("contentManager created")

# Look for ArcGIS items that will be cloned
itemsToClone = contentManager.search("<Search Parameter>") # Search parameter
print("itemsToClone")
print("=================")
print(itemsToClone)

# Print which items were cloned
print("Cloned items")
print("=================")
print (contentManager.clone_items(itemsToClone, folder="<Your folderName>"))
print("Python Scripted completed successfully")