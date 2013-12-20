fields = (["FROMLEFTP", "TORIGHTP", "TOLEFTP", "FROMRIGHTP", "FROMLEFTA",
		   "TORIGHTA", "TOLEFTA", "FROMRIGHTA", "TRAFFIC_FLOW"])

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
		# update swaps
		row[0], row[1] = row[1], row[0]
		row[2], row[3] = row[3], row[2]
		row[4], row[5] = row[5], row[4]
		row[6], row[7] = row[7], row[6]
		
		# swap directions
		if row[8] == 'F':
			row[8] = 'R'
			cursor.updateRow(row)
		elif row[8] == 'R':
			row[8] = 'F'
			cursor.updateRow(row)
		else:
			cursor.updateRow(row)