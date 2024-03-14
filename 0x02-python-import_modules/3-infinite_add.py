#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    result = 0
    if i == 1:
        print("0")
    else:
        for j in range(1, i):
            result = result + int(argv[j])
        print(result)

