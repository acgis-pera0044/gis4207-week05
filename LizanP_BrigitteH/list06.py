import sys
import os

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage:  list06.py <root_folder>')
        sys.exit()

    root_folder = sys.argv[1]

    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist")
        sys.exit()
    
    import arcpy
    
    show_workspace_paths(root_folder)


def show_workspace_paths(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder, topdown = True):
        arcpy.env.workspace = dirpath
        workspaces = arcpy.ListWorkspaces("*")
        for workspace in workspaces:
            print(os.path.abspath(workspace))

if __name__ == '__main__':
    main()