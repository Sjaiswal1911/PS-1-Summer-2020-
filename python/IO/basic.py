# IO basics

# Printing to the screen
#print("statement")
print("Hello, I am printing this on the screen.")


# Reading Keyboard Input
# var_name = input("Prompt")
x = input("Write something >")
print("You enetered :", x)


# Opening a File
# file object_name = open (file_name, [accessmode], [buffering])
# default : accessmode -> 'r' i.e Read
# buffering -> 0 i.e no buffering. 1 -> buffering
fo = open("sample.text",'wb')
# wb creates a file if it doesn't exist and in binary format


#Attributes:

# Closed
# file.closed
# Returns true if the file is cloesd
print("Closed or not:" , fo.closed)


# Name
# file.name
# Returns name of the file
print("Name of the file is:", fo.name)


# Mode
# fo.mode
# returns the mode with which the file was accessed.
print("Opening Mode: ", fo.mode)
