#!/usr/bin/python3

def remove_char_at(str_val, n):
    if n < 0:
        return str_val
    count = 0
    str_copy = ""
    for val in str_val:
        if count == n:
            count += 1
            continue
        str_copy += str_val[count]
        count += 1
    return str_copy
