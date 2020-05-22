from sys import argv

#unpack the argv arguments
script, input_file = argv

#reading data from a file
def print_all(f):
    print(f.read())

#reading a line from the file   
def print_a_line(line_count,f):
    print(line_count,f.readline())

#taking the curosr to the start-of-file    
def rewind(f):
    f.seek(0)

#initalizing the fileIO stream    
current_file = open(input_file)

print("First let's print the whole file ./n")
print_all(current_file)

print("Now let's rewind , kind of like a tape")
rewind(current_file)

print("Let's print all three lines")

currentLine = 1
print_a_line(currentLine,current_file)

currentLine = currentLine + 1
rewind(current_file)
print_a_line(currentLine, current_file)

currentLine = currentLine + 1
print_a_line(currentLine, current_file)
