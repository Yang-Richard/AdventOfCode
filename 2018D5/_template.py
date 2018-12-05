#!/usr/bin/python

filepath = 'test.txt'#'input.txt'

from datetime import datetime
startTime = datetime.now()

def main() -> "result1, result2":
    nums = []
    result1 , result2 = 0, 0
    with open(filepath) as f:
        for line in f.readlines():
            nums.append(line)
        f.close()
        
    print(nums)

    return result1, result2

if __name__ == '__main__':
    print(main(), str(datetime.now() - startTime)[:-3])
