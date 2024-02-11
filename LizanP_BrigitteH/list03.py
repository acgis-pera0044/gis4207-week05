import sys

def main():
    global arcpy

    if len(sys.argv) !=3:
        print('Usage: list03.py <Workspace> feature_type')
        sys.exit()

    import arcpy

    arcpy.env.workspace = sys.argv[1]
    workspace = arcpy.env.workspace

    feature_type = sys.argv[2]

    if not arcpy.Exists(workspace):
        print(f"{workspace} does not exist.")
        sys.exit()
    
    valid_feature_types = ['Annotation',
    'Arc',
    'Dimension',
    'Edge',
    'Junction',
    'Label',
    'Line',
    'Multipatch',
    'Multipoint',
    'Node',
    'Point',
    'Polygon',
    'Polyline',
    'Region',
    'Route',
    'Tic',
    'All']

    if feature_type in valid_feature_types:
        show_feature_classes(feature_type)
    else:
        print(f"{feature_type} does not exist.")


def show_feature_classes(feature_type):
    fcList = arcpy.ListFeatureClasses("", f"{feature_type}")
    for fc in fcList:
        print(fc)

if __name__ == '__main__':
    main()
