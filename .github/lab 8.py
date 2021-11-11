# Programmers: Victoria and Peter
# Course: CS151, Dr. Rajeev
# Date: 11/11/21
# Lab Number: 8
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

import random
names = []


def load_name_list(filename):
    names_file = open(filename, "r")
    for line in names_file:
        names.append(line)
    return names


def pop_random_name(namelist):
    random.shuffle(names)
    name = names[0]
    names.remove(names[0])
    return name


def main():
    chosen_name = pop_random_name(load_name_list("names.txt"))
    print(chosen_name)


main()
