#!/usr/bin/python3
#coding=utf-8

import sys
import os
import random
import time

file = sys.argv[1] if len(sys.argv) > 1 else "todo"
path = "{}/{}.txt".format(os.path.expanduser(os.path.dirname(os.path.abspath(__file__))), file)

with open(path) as f:
    todo = f.read().splitlines()

try:
    i = 1
    rand = random.randint(0, len(todo) - 1)
    start_time = time.time()

    while True:
        input("{}- {}".format(i,todo[rand]))

        print(time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time)))

        i += 1
        rand = random.randint(0, len(todo) - 1)
        start_time = time.time()

except KeyboardInterrupt:
    print()
