#!/usr/bin/env python

import csv
import redis
import sys
from time import sleep

client = redis.Redis(host="localhost", port=6379)


if len(sys.argv) > 2:
    load_file = sys.argv[1]
    stream    = sys.argv[2]
    if len(sys.argv) > 3:
	    sleep_time = int(sys.argv[3])/1000
    else:
	    sleep_time = 0


else:
    load_file = 'cueto_june.csv'


with open(load_file, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		client.xadd(stream, row)
		sleep(sleep_time)

