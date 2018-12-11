#!/usr/bin/python3
# c5.18xlarge (72 vCPU) on Amazon AWS

from datetime import datetime
from multiprocessing import Pool
import numpy as np
startTime = datetime.now()

serial = 3613
size = 300
grid = np.zeros([size,size])
result1 , result2 = 0, 0

def findScore(s):
    scores = []
    highscore = 0
    currentTime = datetime.now()
    for y in range(size-(s-1)):
        for x in range(size-(s-1)):
            score = sum(sum(grid[y:y+s, x:x+s]))
            if score > highscore:
                highscore = score
                scores.append((x+1, y+1, s, highscore))
    print(str(datetime.now() - currentTime), s, highscore)
    return scores
    
def main():
    scores = set()
    for y in range(size):
        for x in range(size):
            newpower = ((x+1+10)*(y+1)+serial)*(x+1+10)
            if len(str(newpower))<3:
                grid[y, x] = -5
            else:           
                grid[y, x] = (int((str(newpower))[-3:-2])-5)
                
    with Pool(72) as p:
        scores = [item for sublist in p.map(findScore, range(1,size+1)) for item in sublist]

    return [a for a in scores if a[2] == 3][-1], max(scores,key=lambda item:item[3])[:3]

if __name__ == '__main__':
    print(main(), str(datetime.now() - startTime)[:-3])