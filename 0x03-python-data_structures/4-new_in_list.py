#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newllist = my_list.copy()
    for items in newllist:
        if(idx < 0):
            return newllist
        elif(idx > len(newllist) - 1):
            return newllist
        else:
            newllist[idx] = element
            return newllist
