#!/usr/bin/env python
import csv

def average(list):
  return reduce(lambda x, y: x + y, list) / len(list)

class Batter:
  def __init__(self, name, hrs, runs, steals):
    self.name = name
    self.homeRuns = hrs
    self.runs = runs
    self.stolenBases = steals

  @staticmethod
  def from_csv_row(row):
    return Batter(row[0], int(row[1]), int(row[2]), int(row[3]))

class Universe:
  def __init__(self, players):
    self.players = players

  def calculate_averages():



f = open('./sample.csv', 'rb')
reader = csv.reader(f)
rownum = 0
header = []
players = []

for row in reader:
  if rownum == 0:
    header = row
  else:
    players.append(Batter.from_csv_row(row)) 
  rownum += 1

print str(len(players)) + ' players.'
  
f.close()
