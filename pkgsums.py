#!/usr/bin/python

import os
import sys

from hashlib import sha256
from pathlib import Path

def main(directory):
	sums = []
	p = Path(directory)
	for item in [x for x in p.iterdir() if x.is_file()]:
		with item.open('rb') as fp:
			h = sha256(fp.read()).hexdigest()
			sums.append((h, item.name))
	print('sha256sums=(')
	for pair in sums:
		print("    '{}' # {}".format(*pair))
	print(')')


if __name__ == '__main__':
	main(sys.argv[1])
