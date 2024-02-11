import sys
import os

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage:  list07.py <root_folder>')
        sys.exit()

    root_folder = sys.argv[1]

    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist")
        sys.exit()
    
    import arcpy
    
    show_workspaces_and_feature_classes(root_folder)


def show_workspaces_and_feature_classes(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder, topdown = True):
        arcpy.env.workspace = dirpath
        workspaces = arcpy.ListWorkspaces("*")
        feature_classes = arcpy.ListFeatureClasses("*")
        for workspace in workspaces:
            print(os.path.abspath(workspace))
        for feature in feature_classes:
            print(os.path.abspath(feature))

if __name__ == '__main__':
    main()