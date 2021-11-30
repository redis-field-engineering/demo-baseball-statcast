#!/usr/bin/env python

import csv
import redis
import sys

client = redis.Redis(host="localhost", port=6379)


if len(sys.argv) > 2:
    load_file = sys.argv[1]
    stream    = sys.argv[2]
else:
    load_file = 'cueto_june.csv'


with open(load_file, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		client.xadd(stream, row)

