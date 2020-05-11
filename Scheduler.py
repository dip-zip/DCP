"""Implement a job scheduler which takes in a function
f and an integer n, and calls f after n milliseconds.
"""

import time

def scheduler(foo,n):
    while True:
        time.sleep(n)
        """Need to fix this as it is not exactly a scheduler"""
        foo()

def hello_world():
    print("Hello World")

scheduler(hello_world, 1)