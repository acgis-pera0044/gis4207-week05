import sys

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage: describe06.py <FeatureClassName>')
        sys.exit()

    fc = sys.argv[1]

    import arcpy
    
    if not arcpy.Exists(fc):
        print(f"{fc} does not exist.")
        sys.exit()
    
    show_description(fc)

def show_description(fc):
    dscFC = arcpy.da.Describe(fc)
    print(f"{'Field Name':15}{'Field Type':>15}{'Length':>9}")
    print(f"{'-'*10:15}{'-'*10:>15}{'-'*6:>9}")
    fields = dscFC['fields']
    for field in fields:
        print(f"{field.name:15}{field.type:>15}{field.length:>8}")

if __name__ == '__main__':
    main()