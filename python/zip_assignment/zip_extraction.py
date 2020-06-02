from zipfile import ZipFile
file_name="ball.zip"
with ZipFile(file_name,'r') as zip:
    print("Extracting all files........")
    zip.extract("messi.txt") #extract specific file
    zip.extractall() #extract all files
    print("Completed process!")
