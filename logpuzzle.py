#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_key(url):#Organiza las url por la tercera palabra si existe
    match = re.search(r'-(\w+)-(\w+)\.\w+', url)
    if match:
        return match.group(2) #retorna la tercera palabra palabra, elemento del segundo parentesis
    else:
        return url


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  separator = filename.index('_') # find the index of the underline in the name of the file
  host = filename[separator + 1:] #Extract the name of the host
  url = {} #for creating the dictionary of the image's url
  
  f = open(filename)
  for line in f:
     match = re.search(r' "GET (\S+)', line) #Encuentra la ruta que esta despues del get y rodeada por espacios
     
     if match:
         path = match.group(1) #Hace referencia al elemento del primer parentesis
         if 'puzzle' in path: #Solo agrega los que pertenezca al puzzle
             url['http://' + host + path] = 1
             
  return sorted(url.keys(), key=sort_key) #key usa como argumento de la funcion las claves
  

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on  
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    html = file(os.path.join(dest_dir, 'index.html'), 'w')
    html.write('<html><body>\n')
    
    i=0
    for url in img_urls:
        filename = 'img%d' % i
        print ("Downloading: ", url)
        urllib.urlretrieve(url, os.path.join(dest_dir, filename))
        
        html.write('<img src="%s">' % (filename,))  
        i += 1
        
    html.write('\n</body></html>\n')
    html.close()
      
  

def main():
    opc = '--todir'
    
    animal_dir = r"animaldir"
    animal_file = r"/Resources/animal_code.google.com"
    
    place_dir = r"placedir"
    place_file = r"Resources/place_code.google.com"
    
    logfile = place_file
    todir  = place_dir    
    
    if opc  == '--todir':
        download_images(read_urls(logfile), todir)
    else:
        print ('\n'.join(read_urls(logfile)))
    
    """  
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)
  """
  

if __name__ == '__main__':
  main()
