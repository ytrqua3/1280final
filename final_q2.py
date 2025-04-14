#!/usr/bin/python3

import sys
import re
data_fname = sys.argv[1]
table_fname = sys.argv[2]
data_str = ""
with open(data_fname, mode="r") as file:
	for line in file:
		data_str += line.strip("\n")

data=data_str.split(")")
table={}
with open(table_fname, mode="r") as file:
	for line in file:
		items=line.strip("\n").split(",")
		table[items[0]]=items[1:]
result_dict={}
for item in data:
	item=item.strip("(").split(",")
	if len(item)!=4:
		continue
	reigon=item[0]
	species=item[1]
	xcoor=float(item[2])
	ycoor=float(item[3])
	try:
		result_dict[reigon]
		#when reigon is found
		try:
			result_dict[reigon][species]
			#when reigon and species are already initialized
			if float(table[reigon][0]) < xcoor and xcoor < float(table[reigon][2]) and float(table[reigon][1]) < ycoor and ycoor < float(table[reigon][3]):
				result_dict[reigon][species] += 1
		except KeyError:
			#when reigon is found but species is not yet initialized
			if float(table[reigon][0]) < xcoor and xcoor < float(table[reigon][2]) and float(table[reigon][1]) < ycoor and ycoor < float(table[reigon][3]):

                                result_dict[reigon][species] = 1
	except KeyError:
		#when the reigon is not yet in the dict, create and add the species count as 1
		result_dict[item[0]]={}
		if float(table[reigon][0]) < xcoor and xcoor < float(table[reigon][2]) and float(table[reigon][1]) < ycoor and ycoor < float(table[reigon][3]):
			result_dict[item[0]][item[1]]=1
result_dict = sorted(result_dict.items())
for key, value in result_dict:
	value = sorted(value.items())
for reigon, species_count in result_dict:
	print("For reigon", reigon)
	for s, c in species_count.items():
		print("\tYou have", c, s, "in the rectangle")
