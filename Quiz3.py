#Quiz 3 (TBD)

def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 0.0
    for i in num_list:
        sum += i
    return sum/len(num_list)

#print(get_average([1,3,5,6,7]))

#Write Python code to write all the strings in the sports list to a file called sports.txt
#with each sport string being on its own line in the file.
sports = ["basketball", "softball", "football", "baseball", "track"]
for i in range(len(sports)):
    sports[i] += "\n"
output_file_name = "sports.txt"
outfile = open(output_file_name, "w")
outfile.writelines(sports)
outfile.close()
    
#Write Python code to read the sports.txt file and print out each line of the file to the terminal. 
input_file_name = "sports.txt"
infile = open(output_file_name, "r")
for line in infile:
    print line
infile.close()


hats = {"snapback": 10, "beanie": 5, "baseballcap": 3}
hats["weird top hat"] = 1
hats["snapback"] += 1
print(hats)
del hats["weird top hat"]
print(hats)

def summation(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number
    return sum

print(summation([4,5,2,-3]))




