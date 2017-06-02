#!/usr/bin/env python
from random import randint

def dice(ct, dlevel, tmod):
  ret = tmod
  for x in range(0, ct - 1):
    ret +=  randint(1, dlevel)
  return ret

class Batter:
  def __init__(self, name, hrs, runs, steals):
    self.name = name
    self.homeRuns = hrs
    self.runs = runs
    self.stolenBases = steals

last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', \
  'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', \
  'Garcia', 'Martinez', 'Robinson']

first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', \
  'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'George']

for ln in last_names:
  for fn in first_names:
    name = fn + ' ' + ln
    hrs = dice(3, 20, -3)
    print name + ': ' + str(hrs)
