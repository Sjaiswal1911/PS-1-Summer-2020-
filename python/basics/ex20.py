from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def print_a_line(line_count,f):
    print(line_count,f.readline())

def rewind(f):
    f.seek(0)

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
