import arcpy

# set workspace to SDE connection
workspace = r"Database Connections\facilities@5160_93.sde"

# set the fields to the ones being flipped
fields = (["TRAFFIC_FLOW"])
fc = "FACILITIES.Centerline"
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
		if row[0] == 'F':
			print 'Forward'
		elif row[0] == 'R':
			print 'Reverse'
		elif row[0] == '0':
			print 'No Flow'
		elif row[0] == '1':
			print 'Clear'