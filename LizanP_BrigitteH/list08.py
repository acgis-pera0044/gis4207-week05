import sys
import os

def main():
    global arcpy

    if len(sys.argv) !=4:
        print('Usage:  list08.py <root_folder> <Point|Polyline|Polygon|> <out_file_name>')
        sys.exit()
    
    root_folder = sys.argv[1]

    feature_type = sys.argv[2]

    out_file_name = sys.argv[3]

    valid_feature_types = ['Point','Polyline','Polygon']

    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist")
        sys.exit()
    elif feature_type not in valid_feature_types:
        print(f"{feature_type} does not exist")
    else:
        import arcpy
        show_feature_classes(root_folder, feature_type, out_file_name)
    

def show_feature_classes(root_folder, feature_type, out_file_name):
    feature_classes = []
    walk = arcpy.da.Walk(root_folder, datatype="FeatureClass", type = feature_type)
    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            feature_classes.append(os.path.join(dirpath, filename))
    
    with open(out_file_name, 'w') as outfile:
        outfile.write(f'{feature_type} feature classes in and below {root_folder}\n')
        for feature in feature_classes:
            outfile.write(f'{feature}\n')

if __name__ == '__main__':
    main()