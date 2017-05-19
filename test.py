#!/usr/bin/python
import sys
import os
a=sys.argv
print(a[1])

f = open("hello.py","r+")
content = f.read()
print(content)