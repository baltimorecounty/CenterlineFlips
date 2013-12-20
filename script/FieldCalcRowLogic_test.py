fc_shp = "CENTERLINE_FLIPS"
field = "FLIP"
desc = arcpy.Describe(fc_shp)
if not desc.FIDSet  == '':
	print 'Flip would happen'
else:
	arcpy.AddMessage("Error.No {0} features are selected.".format(fc_shp))