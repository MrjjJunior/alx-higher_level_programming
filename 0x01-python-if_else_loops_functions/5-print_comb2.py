#!/usr/bin/python3
num = 0
while num < 100:
    if num < 10:
        print(f"0{num},", end=' ')
    else:
        print(f"{num},", end=' ' if num != 99 else "\n")
    num = num + 1
