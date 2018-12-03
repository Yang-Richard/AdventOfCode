#!/usr/bin/python

filepath = 'input.txt'

def main():

	nums = []
	with open(filepath) as f:
        	for line in f.readlines():
            		nums.append(int(line))
        f.close()
	result1 = nums
	
	return result1, result2

if __name__ == '__main__':
	result = main()
   	# print("{},{}".format(result[0], result[1]))
