#!/usr/bin/python3
a = 10
b = 5

if __name__ == '__main__':
    from calculator_1 import add
    print("{} + {} = {}".format(a, b, add(a , b)))

if __name__ == '__main__':
    from calculator_1 import sub
    print("{} - {} = {}".format(a, b, sub(a , b)))

if __name__ == '__main__':
    from calculator_1 import mul
    print("{} * {} = {}".format(a, b, mul(a , b)))

if __name__ == '__main__':
    from calculator_1 import div
    print("{} / {} = {}".format(a, b, div(a , b)))
