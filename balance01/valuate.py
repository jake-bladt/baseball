#!/usr/bin/env python
import csv

class Batter:
  def __init__(self, name, hrs, runs, steals):
    self.name = name
    self.homeRuns = hrs
    self.runs = runs
    self.stolenBases = steals

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
