#!/usr/bin/env python
from __future__ import division
import csv

def average(list):
  return reduce(lambda x, y: x + y, list) / len(list)

class Batter:
  def __init__(self, name, hrs, runs, steals):
    self.name = name
    self.homeRuns = hrs
    self.runs = runs
    self.stolenBases = steals

  def compare_to(self, replacement_player):
    score = self.homeRuns / replacement_player.homeRuns
    score += self.runs / replacement_player.runs
    score += self.stolenBases / replacement_player.stolenBases
    score /= 4.0

    self.score = score
    return score

  @staticmethod
  def from_csv_row(row):
    return Batter(row[0], int(row[1]), int(row[2]), int(row[3]))

class Universe:
  def __init__(self, players):
    self.players = players

  def calculate_averages(self):
    avgHrs = average([p.homeRuns for p in self.players])
    avgRuns = average([p.runs for p in self.players])
    avgSteals = average([p.stolenBases for p in self.players]) 

    self.averagePlayer = Batter('Average', avgHrs, avgRuns, avgSteals)

f = open('./players.csv', 'rb')
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
uni = Universe(players)
uni.calculate_averages()
avg = uni.averagePlayer

print 'The average player has ' + str(avg.homeRuns) + ' home runs, ' + str(avg.runs) + \
  ' runs, and ' + str(avg.stolenBases) + ' steals.'

for p in players:
  print p.name + ' has a score of ' + str(p.compare_to(uni.averagePlayer))

f.close()
