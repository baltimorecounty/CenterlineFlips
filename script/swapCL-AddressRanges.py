import arcpy

workspace = r"Database Connections\5160Facilities.sde"

fields = (["FROMLEFTP", "TORIGHTP", "TOLEFTP", "FROMRIGHTP",
           "FROMLEFTA", "TORIGHTA", "TOLEFTA", "FROMRIGHTA",])

fc = "FACILITIES.Centerline"

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print(("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}"
               .format(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7])))

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:

        row[0], row[1] = row[1], row[0]
        row[2], row[3] = row[3], row[2]
        row[4], row[5] = row[5], row[4]
        row[6], row[7] = row[7], row[6]

        cursor.updateRow(row)
