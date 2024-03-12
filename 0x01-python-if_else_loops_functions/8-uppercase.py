#!/usr/bin/python3
def uppercase(str):
    convert = ord('a') - ord('A')
    for i in str:
        print("{:c}".format(ord(i) - convert if ord(i) >= ord('a')
                            and ord(i) <= ord('z') else ord(i)), end="")
    print("")
