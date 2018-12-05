#!/usr/bin/python
# AdventofCode
# 2017 Day 2 - Nov 17, 2018
# Output: The checksum and row division sum are 32121 and 197.
# Lines: 34
# Characters: 866

import csv
input = 'input.txt'

def main():
	result1, result2 = 0, 0

	with open(input, 'rb') as csv_file:
    		for row in csv.reader(csv_file, delimiter='\t'):
			maxVal = int(row[0])
			minVal = maxVal

			for i in range(len(row)):
				currentVal = int(row[i])
			`	if currentVal > maxVal:
					maxVal = currentVal
				elif currentVal < minVal:
					minVal = currentVal

				for j in range(len(row)):
					if currentVal % int(row[j]) == 0 and not currentVal == int(row[j]):
						result2 += currentVal/  int(row[j])
			result1 += maxVal - minVal 		
	return result1, result2	

if __name__ == '__main__':
	result = main()
	print("The checksum and row division sum are {} and {}.".format(result[0], result[1]))
