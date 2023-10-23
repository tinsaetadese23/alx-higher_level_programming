#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return  ('None')
    lenn = len(my_list) - 1
    while lenn >= 0:
        print("{:d}".format(my_list[lenn]))
        lenn -= 1
