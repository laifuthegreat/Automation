def rm():
	m_list = open('member_list.csv', 'r')
	d_list = open('done_members.csv', 'r')
	o_list = open('to_do.csv', 'w')
	d_ls = []
	for d_line in d_list:
		d_ls.append(d_line)
	for m_line in m_list:
		if not m_line in d_ls:
			o_list.write(m_line)

rm()
