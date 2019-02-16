#!/usr/bin/python

filepath = 'input.txt'

def main():
    nums = []
    sums = {0}
    result1, result2, currentSum = 0, 0, 0
    stillSearching, firstIteration = True, True
    

    with open(filepath) as f:
        for line in f.readlines():
            nums.append(int(line))
        f.close()

    while(stillSearching):
        for val in nums:
            currentSum += int(val)

            if stillSearching and currentSum in sums:
                result2 = currentSum
                stillSearching = False
            sums.add(currentSum)

        if firstIteration:
            result1 = currentSum
            firstIteration = False
        
    return result1, result2

if __name__ == '__main__':
    result = main()
    print("{},{}".format(result[0], result[1]))
