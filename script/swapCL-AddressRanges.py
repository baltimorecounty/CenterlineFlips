import arcpy

from arcpy import env 
import os 

# Establish connection for workspace 

workspace = r"Database Connections\5160Facilities.sde"

fields = ["FROMLEFTP", "TORIGHTP"]

fc = "FACILITIES.Centerline"

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print("{0}, {1}".format(row[0], row[1]))


with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:

        row[0], row[1] = row[1], row[0]

        cursor.updateRow(row)
