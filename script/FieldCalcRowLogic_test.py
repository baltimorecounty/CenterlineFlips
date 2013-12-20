fc_shp = "CENTERLINE_FLIPS"
field = "FLIP"
desc = arcpy.Describe(fc_shp)
if not desc.FIDSet  == '':
	arcpy.CalculateField_management("CENTERLINE_FLIPS","FLIP",'1')
else:
	arcpy.AddError("Error.No {0} features are selected.".format(fc_shp))
	
print(arcpy.GetMessages())