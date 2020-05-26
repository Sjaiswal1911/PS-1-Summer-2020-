# Write operations
# fileObject.write(string)
# here the passed paramter is the content to be written
# Open a file
fo = open("sample.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()


# Read operations
# fileObject.read([count])
# here the count represents the number of bytes to be read.
#!/usr/bin/python3

# Open a file
fo = open("sample.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# to read the whole file
# print("The file says :\n", fo.read())

# Close opened file
fo.close()


# File positions
# fo.tell()
# gives the position of the cursor in the file
# Open a file
fo = open("sample.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)


# Seek positions
# fo.seek(offset[,from])
# from is optional and by defualt the start of file i.e '0'
print("Taking the cursor to the start:")
position = fo.seek(0)


# Reading  a line
# fo. readline()
print("Reading the line..",fo.readline())
print("Closing the file now.")
fo.close()
