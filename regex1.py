'''
Python Regex Script to find Multiline Strings between 2 key words
Takes all txt files in a folder and exports them out to a single consolidated txt file.
'''

import os
import collections
import csv
import re

path = os.getcwd()
files = os.listdir(path)

regex1 = r"(?s)(?<=Input XML).*?(?=Output XML)" #Body of API request I want
regex2 = r"^Main URL\:.*" #API Target URL

files_csv = [f for f in files if f[-3:] == 'txt'] #This runs the script on all txt files in current directory
for f in files_csv:
    requests = open(f,"r")
    requests = requests.read()
    firstline = re.findall(regex2, requests, re.MULTILINE) #re.Multiline is required for strings spanning a few lines
    apiBody = re.findall(regex1, requests)
    apiBody = apiBody[:]
    firstline = firstline[:]
    g = open("consolidated-output.txt", "a") #"a" to append to file
    for x in firstline:
        g.write(x)
    for i in apiBody:
        g.write(i)
    g.close

