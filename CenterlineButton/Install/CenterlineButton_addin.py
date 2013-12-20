import arcpy
import pythonaddins

class SwapCenterlines(object):
    """Implementation for CenterlineButton_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # Script to flip attributes on a centerline.
		# arcpy.da.SearchCursor requires ArcGIS 10.1 or higher
		# coding help via GIS StackExchange:
		# http://gis.stackexchange.com/a/79625/15499
		# http://gis.stackexchange.com/questions/79615/is-there-a-programmatic-way-to-swap-attributes-on-a-feature/79625?noredirect=1#comment109573_79625
		
		try:
			workspace = r"Database Connections\facilities@5160_93.sde" # set workspace to SDE connection
			fields = (["FROMLEFTP", "TORIGHTP", "TOLEFTP", "FROMRIGHTP", "FROMLEFTA",
					   "TORIGHTA", "TOLEFTA", "FROMRIGHTA", "TRAFFIC_FLOW"]) # set the fields to the ones being flipped
			fc = "FACILITIES.Centerline" # set the feature class to the SDE feature class name
			fc_shp = "CENTERLINE_FLIPS" # feature class to calculate
			field = "FLIP" # calc filed to change
			desc = arcpy.Describe(fc_shp) # describe selection of fc_shape

			if not desc.FIDSet  == '': # an fc_shp is selected
				# Marked the discrepancy as done in the CENTERLINE_FLIPS tracking shapefile
				arcpy.CalculateField_management(fc_shp,field,'1')
				
				# loops through selected rows and swaps the values
				with arcpy.da.UpdateCursor(fc, fields) as cursor:
					for row in cursor:
						# flips the line direction
						arcpy.FlipLine_edit("FACILITIES.Centerline")
						
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

			else:
				# this is not working at the moment
				arcpy.AddError("Error. No {0} features are selected.".format(fc_shp))
				print(arcpy.GetMessages())
		except Exception as e:
			arcpy.AddError(e.message)