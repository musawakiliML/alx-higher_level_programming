#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        unicode_value = ord(str[i])
        if unicode_value >= 97 and unicode_value <= 122:
            unicode_value = unicode_value - 32
        print("{}".format(chr(unicode_value)), end='')
    print()
