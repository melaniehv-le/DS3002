#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby babynames exercise

Define the extract_babynames() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
file for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the babynames and rank numbers and just print them
 -Get the babynames data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_babynames list
"""

def extract_babynames(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # LAB(begin solution)
  babynames = []

#opening file
  f = open(filename, 'rU')
  file = f.read()

#extracting the year
  matched = re.search(r'Popularity\sin\s(\d\d\d\d)', file)
  if not matched:
    #If no matched year, give error message
    sys.stderr.write('No Year Matched')
    sys.exit(1)
  year = matched.group(1)
  babynames.append(year)

  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', file)

  rankednames =  {}
  for rank_tuple in tuples:
    (rank, boyname, girlname) = rank_tuple
    if boyname not in rankednames:
      rankednames[boyname] = rank
    if girlname not in rankednames:
      rankednames[girlname] = rank

  sorted_babynames = sorted(rankednames.keys())


  for name in sorted_babynames:
    babynames.append(name + " " + rankednames[name])

  return babynames



def main():
  #started at [1] not [0]
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # LAB(begin solution)
  for filename in args:
    babynames = extract_babynames(filename)

    # Make file from list
    file = '\n'.join(babynames)

    if summary:
      output = open(filename + '.summary', 'w')
      output.write(file + '\n')
      output.close()
    else:
      print(file)


if __name__ == '__main__':
  main()
