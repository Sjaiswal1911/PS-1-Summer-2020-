# display file name

from zipfile import ZipFile
import os

# function to give file paths
def file_paths(directory):
    file_paths=[]
    for root,directories,files in os.walk(directory):
        for filename in files:
            filepath=os.path.join(root,filename)
            file_paths.append(filepath)
        return file_paths

try:
    directory=input()         
    file_pths=file_paths(directory)
    
    print("files are")
    for file in file_pths:
        print(file)
        
except:
    print ((sys.exc_info()[0]),"occured")
else:
    print("Files printed successfully")    
