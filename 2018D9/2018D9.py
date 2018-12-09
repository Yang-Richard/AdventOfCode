#!/usr/bin/python

rules = '427 players; last marble is worth 70723 points'

from datetime import datetime
startTime = datetime.now()

def main(factors):# -> "result1, result2":
    print(factors)
    result = []
    
    for i, val in enumerate(factors):
        players, lastball = '', ''

        players, numballs = int(rules[:rules.index(' ')]), int(rules[rules.index('worth ')+6:rules.index(' points')])
        numballs = numballs * val
        print(players, numballs)
        circle, scores = [0], [0]*players
        currentballposition = 0
        ball = 0
        while (ball <= numballs-1):
            #print('working..')
        #for ball in range(1, numballs+1):
            #print(float(ball)/numballs)
            #if ((float(ball)/numballs)*100)>0.1:
            #    print("%.2f" % ((float(ball)/numballs*100)))
                #print((float(ball)/numballs*100))
                
            ball += 1
            #print(ball)
            
            if ball % 23 == 0 and ball != 0: # special ball
                #print('score', circle)
                #print(ball)
                #print(scores[ball%players-1])
                scores[ball%players-1] += ball  
                if currentballposition >= 7:
                    currentballposition = currentballposition - 7
                else:
                    remove = 7 - currentballposition
                    currentballposition = len(circle) - remove
                #print(len(circle), currentballposition)
                scores[ball%players-1] += circle[currentballposition]
                del circle[currentballposition]
                #print(circle)
                
            else:
                
                if currentballposition <= len(circle) - 2: # same line, or right at the end of the line #
                    #print('sameline far',circle, ball)
                    #print('newline')
                    #print((23-(ball % 23), len(circle)-currentballposition-1, numballs-ball+1))
                    #print(min(23-(ball % 23), len(circle)-2, numballs-ball+1))
                    advancements = min(23-(ball % 23), len(circle)-currentballposition-1, numballs-ball+1) 
                    #print(advancements)
                    #print('advance', advancements, range(1, advancements+1))
                    for i in range(1, advancements+1):
                        circle.insert(currentballposition + i*2, ball)
                        ball +=1
                    ball -= 1
                    currentballposition += advancements*2
                    
                else: 
                    #print('newline',circle, ball)
                    #print('endline')
                    currentballposition = 1
                    circle.insert(currentballposition, ball)
                    
                # ball += ##########\   
        #print(circle)
        #break
        result.append(max(scores))
        #print()
        #print(max(scores))
        #print(circle)
        
            
    return result

if __name__ == '__main__':
    
    print(main((1,0)), str(datetime.now() - startTime)[:-3])
    #0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15
    #0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15
    #0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15 
    #0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 
    