fc_shp = "CENTERLINE_FLIPS"
field = "FLIP"
count = arcpy.GetCount_management(fc_shp)
if count >= 1:
	arcpy.CalculateField_management(fc_shp,field,'1')
else:
	arcpy.AddMessage("Error.No {0} features are selected.".format(fc_shp))