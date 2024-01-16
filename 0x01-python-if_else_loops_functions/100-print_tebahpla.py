#!/usr/bin/python3
for j in range(ord('z'), ord('a') - 1, -1):
    if j % 2 == 0:
        digi = 0
    else:
        digi = 32
    print("{}".format(chr(j - digi)), end="")
