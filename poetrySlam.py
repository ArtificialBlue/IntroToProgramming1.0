#Poetry Slam Assignment
import random

def get_file_lines(filename):
    input_file_name = filename
    infile = open(input_file_name, "r")
    return infile.readlines()



def lines_printed_backwards(lines_list):
    counter = len(lines_list)
    for line in reversed(lines_list):
        print(str(counter) + " " + line)
        counter -= 1

#lines_printed_backwards(get_file_lines("The-Jumblies.txt"))

def lines_printed_random(lines_list):
    counter = 1
    for i in range(len(lines_list)):
        print(str(counter) + " " + lines_list[random.randint(0, len(lines_list) - 1)])
        counter += 1

#lines_printed_random(get_file_lines("The-Jumblies.txt"))

def lines_printed_custom(lines_list):
#Sorts by Line Length, using the built-in Python function sort() and using the key of Length
#to sort the lines
    counter = 1
    lines_list.sort(key = len)
    for line in lines_list:
        print(str(counter) + " " + line)
        counter += 1

#lines_printed_custom(get_file_lines("The-Jumblies.txt"))
