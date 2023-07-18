#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
#import commands -> Only works in Unix
import subprocess #replace import commands

"""Copy Special exercise
"""
# Write functions and modify main() to call them
def get_special_paths(direc):
    abspath = []
    paths = os.listdir(direc)
    
    for filename in paths:
        match = re.search(r'__(\w+)__',filename)
        if match:
            abspath.append(os.path.abspath(os.path.join(direc,filename)))
    
    return abspath

def copy_to(paths,to_dir):
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
        print ("not")
    
    for path in paths:
         #fname = os.path.basename(path)
         #shutil.copy(path, os.path.join(to_dir, fname))
        shutil.copy(path,to_dir)
    
    
def zip_to(paths,zipfile):
    cmd = 'zip -r ' + zipfile + ' ' + ' '.join(paths) 
    print ("Command to run:", cmd)
    try:
        output =subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print ("Command error: " + e.output)
        print ("Command output: " + output)
        sys.exit(e.returncode)
        
    """ Only in unix
    #(status, output) = commands.getstatusoutput(cmd)  
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    """
    print ("Sucessful")

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.
  direc = "."
  todir = r"C:\PYTHON\copyspecial\tmp\fooby"
  tozip = r"C:\PYTHON\copyspecial\tmp\fooby\tmp.zip"#no\way.zip"
  
  opc = "--todir"
  if opc == "--todir":
      copy_to(get_special_paths(direc),todir)
      print ("Copied")
  elif opc == "--tozip": #Doesn't work in windows 
      zip_to(get_special_paths(direc),tozip)
  else:
      print ('\n'.join(get_special_paths(direc)))
  """
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  """

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
