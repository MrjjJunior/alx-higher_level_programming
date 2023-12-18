#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    point = 0

    for i in range(x):
        try:
            print("{}".fromat(my_list[i], end="")
            point = point + 1
        except IndexError:
                  break
    print("")
    return (point)
