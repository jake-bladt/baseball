#!/usr/bin/env python

last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', \
  'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', \
  'Garcia', 'Martinez', 'Robinson']

first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', \
  'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'George']

for ln in last_names:
  for fn in first_names:
    print fn + ' ' + ln
