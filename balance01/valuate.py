#!/usr/bin/env python
import csv

class Batter:
  def __init__(self, name, hrs, runs, steals):
    self.name = name
    self.homeRuns = hrs
    self.runs = runs
    self.stolenBases = steals

  @staticmethod
  def from_csv_row(row):
    return Batter(row[0], int(row[1]), int(row[2]), int(row[3]))

f = open('./sample.csv', 'rb')
reader = csv.reader(f)
rownum = 0
header = []
players = []

for row in reader:
  if rownum == 0:
    header = row
  else:
    players.push(Batter.from_csv_row(row)) 
  rownum += 1

print str(len(players)) + ' players.'
  
f.close()
