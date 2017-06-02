#!/usr/bin/env python
import csv

f = open('sample.csv', 'rb')
reader = csv.reader(f)
for row in reader:
  print row

f.close()
