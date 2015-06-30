import csv
import shlex

network_dict = {}
network_dict[1] = 'Facebook'
network_dict[2] = 'Twitter'
network_dict[3] = 'YouTube'
network_dict[4] = 'LinkedIn'
network_dict[5] = 'RSS'

def convert():
	o_init = open('io/output/o_file.csv', 'r')
	input_file = open('io/input/member_list.csv', 'r')
	o_out = open('io/output/converted_file.csv', 'w')
	o_writer = csv.writer(o_out, quoting=csv.QUOTE_ALL)
	o_reader = csv.reader(o_init, skipinitialspace=True)
	i_reader = csv.reader(input_file, skipinitialspace=True)
	i_dict = {}
	for i_line in i_reader:
		print(i_line)
		i_dict[i_line[1]] = i_line[0]
	for o_line in o_reader:
		i = 1
		if o_line[0] in i_dict:
			while i < len(o_line):
				o_wr_ls = []
				o_wr_ls.append(i_dict[o_line[0]])
				o_wr_ls.append(o_line[0])
				o_wr_ls.append(network_dict[i])
				o_wr_ls.append(o_line[i])
				o_writer.writerow(o_wr_ls)
				i += 1

convert()