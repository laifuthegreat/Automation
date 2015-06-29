import csv

network_dict = {}
network_dict[1] = 'Facebook'
network_dict[2] = 'Twitter'
network_dict[3] = 'YouTube'
network_dict[4] = 'LinkedIn'
network_dict[5] = 'RSS'

def convert():
	o_init = open('io/output/o_file.csv', 'r')
	input_file = open('io/input/member_list.csv', 'r')
	o_out = open('io/input/converted_file.csv', 'w')
	o_writer = csv.writer(o_out, quoting=csv.QUOTE_ALL)
	i_dict = {}
	for i_line in input_file:
		i_ls = i_line.split(',')
		i_dict[i_ls[1]] = i_ls[0]
	for o_line in o_init:
		o_ls = o_line.split(',')
		i = 1
		while i < len(o_ls):
			o_wr_ls = []
			for key in i_dict:
				if 'California State Univ' in key:
					print(key)
			o_wr_ls.append(i_dict[o_ls[0]])
			o_wr_ls.append(o_ls[0])
			o_wr_ls.append(network_dict[i])
			o_wr_ls.append(o_ls[i])
			o_writer.writerow(o_wr_ls)

convert()