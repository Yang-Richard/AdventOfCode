#!/usr/bin/python

import json

filepath = 'input.txt'

def main():
	nums = []
	with open(filepath) as f:
       		for line in f.readlines():
			nums.append(line[:-1])
        f.close()

	doub, trip = 0, 0
	for i in nums:
		two, three = False, False
		for j in i:
			if i.count(j) == 2:
				two = True
			if i.count(j) == 3:
				three = True
		doub += two
		trip += three
	result1 = doub*trip
	
	matching = []
	wrongChar = None

	for i in nums:
		for j in nums:
			currentlyMatching, mustMatch = 0, len(i)-1
			for k in range(len(i)):
				if i[k] == j[k]:
					currentlyMatching += 1
				else:
					missing = k
			if currentlyMatching == mustMatch:
				matching.append(str(i))	
				wrongChar = missing	
		if len(matching) == 2:
			break
	result2 = matching[0][:wrongChar] + matching[0][wrongChar+1:]
	return result1, result2

if __name__ == '__main__':
	result = main()
    	print("{},{}".format(result[0], result[1]))
