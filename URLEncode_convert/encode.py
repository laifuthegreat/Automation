import urllib.parse
import csv

f = open("io/input/temp_thing.csv", 'r')
o_f = open("io/output/encoded_file.csv", 'w')
o_writer = csv.writer(o_f, quoting=csv.QUOTE_ALL)
f_reader = csv.reader(f, skipinitialspace=True)
for line in f_reader:
	line[5] = urllib.parse.quote_plus(line[5])
	o_writer.writerow(line)