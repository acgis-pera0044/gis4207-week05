import arcpy

arcpy.env.workspace = "..\..\..\..\data\SanFrancisco"

fcList = arcpy.ListFeatureClasses()

for fc in fcList:
    print(fc)

