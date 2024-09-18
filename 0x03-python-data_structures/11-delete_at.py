#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    for idx in my_list:
        if idx < 0 and idx > 0:
            return (len(my_list(idx[0])))
        else:
            new_list = my_list.del(idx)
            return (new_list)
