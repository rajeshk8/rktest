#!/usr/bin/env python
from __future__ import print_function

## Open the file with read only permit
f = open('redele.txt', "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.readlines()

## close the file after reading the lines.
f.close()


print(lines)



## Open the file with read only permit
f = open('redele.txt')
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    print (line)
    line = f.readline()
f.close()
