#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = "Shaquon with online help"
__help_sources__ = "github: kastnerkyle"
import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

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
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]"""

  # +++your code here+++
  # LAB(begin solution)
  # The list [year, name_and_rank, name_and_rank, ...] we'll eventually return.
    names = []

    # Open and read the file.
    with open(filename) as f:
        text = f.read()
    # Could process the file line-by-line, but regex on the whole text
    # at once is even easier.

    # Get the year.
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        # We didn't find a year, so we'll exit with an error message.
        raise ValueError("Couldn't find year")
        
    year = year_match.group(1)
    names.append(year)

    # Extract all the data tuples with a findall()
    # each tuple is: (rank, boy-name, girl-name)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
    # print tuples

    # Store data into a dict using each name as a key and that
    # name's rank number as the value.
    # (if the name is already in there, don't add it, since
    # this new rank will be bigger than the previous rank).
    names_to_rank = {}
    for rank, boyname, girlname in tuples:
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank
  # You can also write:
  # for rank, boyname, girlname in tuples:
  #   ...
  # To unpack the tuples inside a for-loop.

  # Get the names, sorted in the right order
    sorted_names = sorted(names_to_rank.keys())

  # Build up result list, one element per line
    for name in sorted_names:
        names.append(name + " " + names_to_rank[name])

    return names
  # LAB(replace solution)
  # return
  # LAB(end solution)


def create_parser():
    parser = argparse.ArgumentParser(description='Processes baby names files')
    parser.add_argument('--summaryfile', action='store_true',
                        help="help create summary file")
    parser.add_argument('files', nargs='+', help="filename(s) to parse")
    return parser


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    parser = create_parser()
    args = parser.parse_args()
    print(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = args.summaryfile
    file_list = args.files

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    # LAB(begin solution)
    for filename in file_list:
        print("working on file: {}".format(filename))
        names = extract_names(filename)

        # Make text out of the whole list
        text = '\n'.join(names)

        if summary:
            with open(filename + '.summary', 'w') as outf:
                outf.write(text + '\n')
            
        else:
            print(text)
        # LAB(end solution)


if __name__ == '__main__':
    main()
