#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    every = dir()
    for i in range(0, len(every)):
        if every[i][:2] != "__":
            print("{:s}".format(every[i]))
