#!/usr/bin/python3
def no_c(my_string):
    llist = list(my_string)
    for items in llist:
        if items == 'c' or items == 'C':
            llist.remove(items)
    my_string = "".join(llist)
    return my_string
