import arcpy

fc = "..\..\..\..\data\Canada\province.shp"
dscFC = arcpy.Describe(fc)
print(f'BaseName: {dscFC.Basename}')
print(f'CatalogPath: {dscFC.CatalogPath}')
print(f'DataType: {dscFC.DataType}')