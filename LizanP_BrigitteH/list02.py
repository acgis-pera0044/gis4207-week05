import sys

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage: list02.py <Workspace>')
        sys.exit()
    
    import arcpy

    arcpy.env.workspace = sys.argv[1]
    workspace = arcpy.env.workspace

    if not arcpy.Exists(workspace):
        print(f"{workspace} does not exist")
        sys.exit()
    
    show_feature_classes()


def show_feature_classes():
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList:
        print(fc)

if __name__ == '__main__':
    main()
