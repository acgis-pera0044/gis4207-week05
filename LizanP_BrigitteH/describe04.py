import sys

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage: describe04.py <FeatureClassName>')
        sys.exit()

    fc = sys.argv[1]

    import arcpy
    
    show_description(fc)

def show_description(fc):
    dscFC = arcpy.da.Describe(fc)
    print(f"{'BaseName':13}: {dscFC['baseName']}")
    print(f"{'CatalogPath':13}: {dscFC['catalogPath']}")
    print(f"{'DataType':13}: {dscFC['dataType']}")

if __name__ == '__main__':
    main()