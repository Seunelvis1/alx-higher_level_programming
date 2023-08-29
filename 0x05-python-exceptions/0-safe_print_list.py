#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """It will print x elememts of a list.

    Args:
        my_list (list): is the list to print elements from.
        x (int): is the number of elements of my_list to print.

    Returns:
        The numbers of element printed.
    """
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
