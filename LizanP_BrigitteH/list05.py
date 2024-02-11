import sys
import os

def main():

    if len(sys.argv) !=2:
        print('Usage: list05.py <root_folder>')
        sys.exit()
    
    root_folder = sys.argv[1]

    if not os.path.exists(root_folder):
        print(f"{root_folder} does not exist")
        sys.exit()
    
    show_folders(root_folder)

def show_folders(root_folder):
    for dirPath, dirNames, fileNames in os.walk(root_folder):
        for dir in dirNames:
            print(dir)
    
if __name__ == '__main__':
    main()