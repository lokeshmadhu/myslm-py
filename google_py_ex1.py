#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Modified by Lokesh Madhu as part of online class exercise Dec 2017

import sys
import re

def extract_names(filename):
    namelist = []
    try:
        fnhandle = open(filename, 'rU')        
    except FileNotFoundError:
        print("The {} is not a valid filename. Try again".format(filename))
        sys.exit(1)
    
    else:
        for line in fnhandle:
            yearstr = re.search(r'<h3 align=.* (\d\d+)</h3>', line)# LM-> Searches for year and stores in group 1 
            
            if yearstr:
                #year = re.search(r'(\d\d+)', yearstring.group())
                namelist.append(yearstr.group(1))
            # LM-> grouping the order and the names to make retrieval easy with tuples 'name'.
            # Each tuple will have name order, boy name and the girl name as element of tuple.
            name = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line) 
            if name:
                namelist.append(name[0][1] + " " + name[0][0])
                namelist.append(name[0][2] + " " + name[0][0])
                namelist.sort()
        fnhandle.close()
        return(namelist)


def summaryfile(filename, nameslist):
    try:
        filehandle = open(filename, 'w')
    except:
        print('Unable to open {}'.format(filename))
    else:
        filehandle.write(str(nameslist))
        filehandle.close()

def main():
    # This command-line parsing code is provided by google
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print( 'usage: [--summaryfile] file [file ...]')
        sys.exit(1)

        # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    #
    # LM-> Adding my code to solve the problem. 
    sortednames = []
    # LM-> Change the path name and the filename to your environment.
    # Primarily the file captures all the names, so that you can search for a name to find the
    # trend in baby naming.
    
    #LM-> Change this path to something where you want to create the file.
    summaryfilename = "I:\Documents\Lokesh's Documents\Python Programming\My Programs\summaryfile.txt"
    
    for filename in args[0:]:
        sortednames.append(extract_names(filename))    
    
    # LM-> If summary is set to true, then instead of printing on screen, the names are copied to a file.
    if summary:
        summaryfile(summaryfilename, sortednames)
    else:
        print(sortednames)
      

if __name__ == "__main__": main()