# Script to flip attributes on a centerline.
# arcpy.da.SearchCursor requires ArcGIS 10.1 or higher
# coding help via GIS StackExchange:
# http://gis.stackexchange.com/a/79625/15499
# http://gis.stackexchange.com/questions/79615/is-there-a-programmatic-way-to-swap-attributes-on-a-feature/79625?noredirect=1#comment109573_79625

import arcpy

# set workspace to SDE connection
workspace = r"Database Connections\5160Facilities.sde"

# set the fields to the ones being flipped
fields = (["FROMLEFTP", "TORIGHTP", "TOLEFTP", "FROMRIGHTP",
           "FROMLEFTA", "TORIGHTA", "TOLEFTA", "FROMRIGHTA",])

# set the feature class to the SDE feature class name
# use ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset})
# 	to get a list of feature classes
fc = "FACILITIES.Centerline"

# searches for the cursors to verify the correct data is selected
# uncomment if verification is needed
# with arcpy.da.SearchCursor(fc, fields) as cursor:
#     for row in cursor:
#         print 'FROMLEFTP = {0} ... TORIGHTP = {1}\nTOLEFTP = {2} ... FROMRIGHTP = {3}\nFROMLEFTA = {4} ... TORIGHTA = {5}\nTOLEFTA = {6} ... FROMRIGHTA = {7}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

# loops through selected rows and swaps the values
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:

        row[0], row[1] = row[1], row[0]
        row[2], row[3] = row[3], row[2]
        row[4], row[5] = row[5], row[4]
        row[6], row[7] = row[7], row[6]

        cursor.updateRow(row)
