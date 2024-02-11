import sys

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage: list04.py <root_folder>')
        sys.exit()
    
    import arcpy

    root_folder = sys.argv[1]

    if not arcpy.Exists(root_folder):
        print(f"{root_folder} does not exist.")
        sys.exit()
    
    show_workspaces(root_folder)


def show_workspaces(root_folder):
    arcpy.env.workspace = root_folder
    workspace_list = arcpy.ListWorkspaces('*')
    print(workspace_list)

if __name__ == '__main__':
    main()