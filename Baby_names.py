#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

#import sys
import re

"""Baby Names exercise

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
def posicion(pos,fl):
    count = 0
    for x in fl[pos:]:
        if x != "<":           
            count += 1
        else:
            break
    return count
    
def rank_names(fl):
    fl = fl[:fl.find("/td>\n<tr><td colspan=\"3\"><small>Note:")]
    
    names_lst = [] 
    rank = 0
    pos_an = fl.find("Popularity in ") +14
    year = fl[pos_an:pos_an+4]
    names_lst.append(year)
    
    while len(fl) > 1:
        
        pos_rank = fl.find("<tr align=\"right\"><td>")+22
        if int(rank) < 9:            
            rank = fl[pos_rank]
        elif int(rank) < 99:
            rank = fl[pos_rank:pos_rank+2]
            pos_rank += 1
        elif int(rank) < 999:
            rank = fl[pos_rank:pos_rank+3]
            pos_rank += 2
        else:
            rank = fl[pos_rank:pos_rank+4]
            pos_rank += 3
          
        pos_name1 = pos_rank + 10   
        pos_name2 = pos_name1 + posicion(pos_name1,fl)  
        name1 = fl[pos_name1:pos_name2]
        names_lst.append(name1 + ' ' + rank)
    
        pos_name2 += 9     
        pos_final = pos_name2 + posicion(pos_name2,fl)
        name2 = fl[pos_name2:pos_final] 
        names_lst.append(name2 + ' ' + rank)
        
        fl = fl[pos_final:]
        
    return names_lst 

def rank_names_regex(readed):
    names = []

    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', readed)   
    year = year_match.group(1)
    names.append(year)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', readed)
    names_to_rank =  {}

    for rank_tuple in tuples:
        (rank, boyname, girlname) = rank_tuple  # unpack the tuple into 3 vars
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank
    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:
        names.append(name + " " + names_to_rank[name])

    return names

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    my_file = open(filename,newline='')
    read_file = my_file.read()
    my_file.close()
    #print (read_file)
     
    list_names = rank_names(read_file)
    list_names2 = rank_names_regex(read_file)
    
    text = '\n'.join(sorted(list_names))   
    print(text)
    text2 = '\n'.join(list_names2)
    print(text2)

def main():
  """
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  """
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  extract_names("Resources/baby1994.html")
  
if __name__ == '__main__':
  main()
