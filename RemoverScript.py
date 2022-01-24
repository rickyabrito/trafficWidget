#!/usr/bin/env python3

import re
import os
import sys


def rm_files(ext, direct):
	temp = []
	for root, dirs, files in direct:
		for name in files:
			temp.append(os.path.join(root, name))
		for name in dirs:
			temp.append(os.path.join(root, name))

	print(temp)


ext = ".txt"
path1 = os.walk('./Desktop/')
temp1 = []
for root, dirs, files in path1:
	for name in files:
		temp1.append(os.path.join(root, name))
	for name in dirs:
		temp1.append(os.path.join(root, name))
#rm_files(ext, direct)

print(temp1)
