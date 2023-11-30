#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argLen = len(sys.argv)

    if argLen != 0:
        for i in range(1, argLen):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments")
