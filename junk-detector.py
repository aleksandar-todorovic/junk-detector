#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path

reload(sys)

sys.setdefaultencoding('utf8')

# Feel free to add other dictionaries if you want to.
accepted_russian_chars = [u'а', u'б', u'в', u'г', u'д', u'е', u'ё', u'ж', u'з', 'и', u'й', u'к', u'л', u'м', u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ъ', u'ы', u'ь', u'э', u'ю', u'я']
accepted_english_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
accepted_other = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '-', ' ']

output = []

def analyze_file(filename):
    with open(filename, 'r') as f:
        no_of_russian = 0
        no_of_english = 0
        no_of_other = 0
        total_chars = 0

 	# Uncomment the next line if you want to skip the first line in a file
	# next(f)
        for line in f:
            line = line.decode("utf-8")
            line = line.lower()
            for character in line:
                if character in accepted_russian_chars:
                    no_of_russian = no_of_russian + 1
                elif character in accepted_english_chars:
                    no_of_english = no_of_english + 1
                elif character not in accepted_other:
                    no_of_other = no_of_other + 1


        total_chars += no_of_russian + no_of_english + no_of_other
    try:
	output.append(filename + ',' + str(round(100 * float(no_of_russian) / total_chars, 2)) + ',' + str(round(100 * float(no_of_english) / total_chars, 2)) + ',' + str(round(100 * float(no_of_other) / total_chars, 2)) + '\n')
    except:
	print sys.exc_info()[0]


    # Change the location if you want to output the results somewhere else.
    with open('/tmp/output.csv', 'w') as f:
        f.write('"Name of the file","Percentage of Russian chars","Percentage of English chars","Percentage of others"\n')
        for strings in output:
            f.write(strings)

def analyze_directory():
    # If you want to analyze some other directory instead of the directory you're currently in, 
    # just change "." with the path to that directory.
    for dirpath, dirnames, filenames in os.walk("."):
	# If you want to analyze the files with a specific extension (in this case .txt), 
	# change "[f for f in filenames]" to "[f for f in filenames if f.endswith(".txt")]".
        for filename in [f for f in filenames]:
            fname = os.path.join(dirpath, filename)
            print "Working on " + fname
            analyze_file(fname)

analyze_directory()
