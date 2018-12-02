#!/usr/bin/python

filepath = '.txt'

def main(var):
	with open(filepath) as f:
        for line in f.readlines():
            nums.append(int(line))
        f.close()

    return result1, result2

if __name__ == '__main__':
	result = main()
    print("{},{}".format(result[0], result[1]))
