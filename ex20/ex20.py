from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def seek(f):
    f.seek(0)


def print_a_line(line, f):
    print line, f.readline()

current_file = open(input_file)
print_all(current_file)
seek(current_file)

print_a_line(1, current_file)
print_a_line(2, current_file)
