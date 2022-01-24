#!/usr/bin/env python3
import random
import sys

def create_files(count):
	for x in range(count):
		with open("Random_file{}.txt".format(x), 'w+') as f:
			f.write("This is random file \#{}! Crazy what automation can do no?".format(x))
			f.close()

count = random.randint(1,10)
create_files(count)
