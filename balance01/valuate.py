#!/usr/bin/env python
import csv

f = open('./sample.csv', 'rb')
reader = csv.reader(f)
rownum = 0
header = []

for row in reader:
  if rownum == 0:
    header = row
  else:
    print row 
  rownum += 1
  
f.close()
