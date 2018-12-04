#!/usr/bin/python

filepath = 'input.txt'

def main():
    nums = []
    result1 , result2 = 0, 0
    with open(filepath) as f:
        for line in f.readlines():
            nums.append(line)
        f.close()
        
    print(nums)

    return result1, result2

if __name__ == '__main__':
    print(main())
