data='From stephen.maquard@uct.ac.za Sat Jan 5 09:14:16 2008'
data_list=data.split()
postion=data_list[1].find('@')
data_slice=data_list[1][postion+1:]
address_split=data_slice.split('.')
print(address_split)
