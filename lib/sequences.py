#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    fib_list = [0, 1] 
    for i in range(2, length):
        next_num = fib_list[i-1] + fib_list[i-2] 
        fib_list.append(next_num)
    print(fib_list)
