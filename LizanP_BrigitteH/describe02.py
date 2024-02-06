import arcpy

fc = "..\..\..\..\data\Canada\province.shp"
dscFC = arcpy.Describe(fc)

print(f'{"BaseName":13}: {dscFC.BaseName}')
print(f'{"CatalogPath":13}: {dscFC.CatalogPath}')
print(f'{"DataType":13}: {dscFC.DataType}')