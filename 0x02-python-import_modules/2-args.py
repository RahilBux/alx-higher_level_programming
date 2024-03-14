#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(i - 1))
        for j in range(1, i):
            print("{}: {}".format(j, argv[j]))
