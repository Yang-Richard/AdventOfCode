#!/usr/bin/python

filepath = 'input.txt'
from datetime import datetime
startTime = datetime.now()

def main():
    nums = []
    sums = {0}
    result1, currentSum = 0, 0
    firstIteration = True
    
    with open(filepath) as f:
        for line in f.readlines():
            nums.append(int(line))
        f.close()

    while(True):
        for val in nums:
            currentSum += int(val)

            if  currentSum in sums:
                return result1, currentSum
           
            sums.add(currentSum)

        if firstIteration:
            result1 = currentSum
            firstIteration = False
        
if __name__ == '__main__':
    print(main(), str(datetime.now() - startTime)[:-3])