# Programmers: Victoria and Peter
# Course: CS151, Dr. Rajeev
# Date: 11/11/21
# Lab Number: 8
# Program Inputs: None
# Program Outputs: Random name

# import random and defines names list
import random
names = []


# Loads the file and places the names in a list
def load_name_list(filename):
    names_file = open(filename, "r")
    for line in names_file:
        names.append(line)
    return names


# randomizes and chooses a name, removing it from the list
def pop_random_name(namelist):
    random.shuffle(names)
    name = names[0]
    names.remove(names[0])
    return name


# runs the program and prints a name
def main():
    chosen_name = pop_random_name(load_name_list("names.txt"))
    print(chosen_name)


main()
