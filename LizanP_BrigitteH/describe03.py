import arcpy
import sys

def main():
    if len(sys.argv) !=2:
        print('Usage: describe03.py <FeatureClassName>')
        sys.exit()
    
    fc = sys.argv[1]

    show_attributes(fc)

def show_attributes(fc):
    dscFC = arcpy.da.Describe(fc)
    print(f"{'BaseName':13}: {dscFC['baseName']}")
    print(f"{'CatalogPath':13}: {dscFC['catalogPath']}")
    print(f"{'DataType':13}: {dscFC['dataType']}")

if __name__ == '__main__':
    main()