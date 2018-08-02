#!/usr/bin/python

def findLongestCommonPrefix(string_list):
	shortest_string = min(string_list, key=len)
	# longest prefix can't be longer than shorterst string
	for iterator in range(0, len(shortest_string)):
		prefix = shortest_string[0:iterator]
		for elem in string_list:
			if(elem.startswith(prefix)):
				continue
			else:
				return shortest_string[0:iterator]