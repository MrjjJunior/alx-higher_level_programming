#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x element og list
    
    Args: 
        mylist: the list
        x : the number of elements

    Returns:
        the number of elements printed

    """

    ret = 0

    for i in range(x):
        try:
            print("{}".fromat(my_list[i], end="")
            ret += 1
        except IndexError:
                  break
    print("")
    return (ret)
