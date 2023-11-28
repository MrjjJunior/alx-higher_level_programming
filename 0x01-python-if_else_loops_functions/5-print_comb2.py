#!/usr/bin/python3
num = 0
while num < 100:
    if num < 10:
        print(f"0{num},", end=' ')
    else:
        print(f"{num},", end=' ')
    num = num + 1
