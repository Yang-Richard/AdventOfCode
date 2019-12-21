# REAL ATTEMPT AT PT 2

import numpy, sys, copy
from datetime import datetime
startTime = datetime.now()
grid = numpy.zeros((0, 0))

ADJACENTS = {(0, -1), (0, 1), (-1, 0), (1, 0)}
    
# assumption, each path only has one input/output, ie you cant branch off twice in one level
def pathfind(start, unvisited_orig, outer_orig, inner_orig, grid, end, level, max_level):
    unvisited = unvisited_orig.copy()
    #print('current level', level, start)
    
    new_outs = []
    
    if level == max_level:
        #print('layer limit exceeded', new_outs)
        return None
    
    if level == 0:
        outer = {}
        unvisited[start] = 0
        # remove all outer walls 
    else:
        outer = outer_orig.copy()
        (start_pos,) = outer[start]
        #print(start_pos, unvisited[start_pos])
        del outer[start]
        unvisited[start_pos] = 0
        
        # remove aa and end walls

    for key, val in outer:
        if start == val:
            del outer[key]
            break

    inner = inner_orig.copy()

    while unvisited:
        cur_pos = (list(unvisited.keys()))[0]
        cur_dis = unvisited[cur_pos]
        for key in unvisited.keys():
            if unvisited[key] < cur_dis:
                cur_pos = key
                cur_dis = unvisited[key]
            
        if cur_dis == float('inf'):
            #print('all spots are infinite', level)
            return new_outs
                
        if cur_pos == end and level == 0:
            print('END FOUND', cur_dis, max_level)
            #return 'SUCCESSFUL EXIT'
        
        #print(level, cur_pos, cur_dis)

        for adjacent in ADJACENTS:
            y = cur_pos[0] + adjacent[0]
            x = cur_pos[1] + adjacent[1]

            if grid[y][x].isalpha():
                yy = y + adjacent[0]
                xx = x + adjacent[1]
                key = ''.join(sorted(grid[y][x] + grid[yy][xx]))
                
                if key != 'AA' and key != 'ZZ' and key in outer.keys() and cur_pos in outer[key]:
                    new_outs.append((key, cur_dis + 1))
                    #print('adding new out', (key, cur_dis + 1))
                    continue
                    # return position on inside, extra distance
                    
                if key != 'AA' and key != 'ZZ' and key in inner.keys() and cur_pos in inner[key]:
                    #print('entering new layer', key)
                    returned_portals = pathfind(key, unvisited_orig, outer_orig, inner_orig, grid, None, level + 1, max_level)
                    #print('returned to layer', level, returned_portals)
                    #if level == 4:
                    #    print('halt here')
                    #    print(outer, inner)
                    if returned_portals != None:
                        del inner[key]
                        for portal in returned_portals:
                            (returned,) = inner[portal[0]]
                            unvisited[returned] = cur_dis + 1 + portal[1]
                            del inner[portal[0]]
                    
                    continue
                    
            for key in unvisited.keys():
                if key == (y, x) and unvisited[key] > cur_dis + 1:
                    unvisited[key] = cur_dis + 1
                    break
                
        del unvisited[cur_pos]
    
    #print('returning to last layer', new_outs)
    return new_outs

    #print('FATAL ERROR')

grid = [] 
with open('input.txt', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip('\n'))
        
from collections import defaultdict
unvisited = {}
portals = defaultdict(set)
outer = defaultdict(set)
inner = defaultdict(set)
start, end = None, None 

ADJACENTS = {(0, -1), (0, 1), (-1, 0), (1, 0)}

for y, line in enumerate(grid):
    for x, pos in enumerate(line):
        if pos == '.':
            unvisited[y, x] = float('inf')
            
        if pos.isalpha():
            portal = pos
            for adjacent in ADJACENTS:
                xx, yy = x + adjacent[0], y + adjacent[1]
                if 0 <= xx < len(line) and 0 <= yy < len(grid) and grid[yy][xx].isalpha():
                    portal = ''.join(sorted(pos + grid[yy][xx]))
                    xx, yy = xx + adjacent[0], yy + adjacent[1]
                    if portal == 'AA' and start == None and 0 <= xx < len(line) and 0 <= yy < len(grid) and grid[yy][xx] == '.':
                        start = (yy, xx)
                    elif portal == 'ZZ' and end == None and 0 <= xx < len(line) and 0 <= yy < len(grid) and grid[yy][xx] == '.':
                        end = (yy, xx)
                    else:
                        if 0 <= xx < len(line) and 0 <= yy < len(grid) and grid[yy][xx] == '.':
                            portals[portal].add((yy, xx))   
                            
                            if yy == 2 or yy == len(grid) - 3 or xx == 2 or xx == len(line) - 3:
                                outer[portal].add((yy, xx))   
                            else:
                                inner[portal].add((yy, xx))   

#print(unvisited)
#print(portals)
print(start, end)
print(outer)
print(inner)
#print(pathfind(start, end, unvisited, portals, grid))

for i in range(15, 50):
    print(i)
    pathfind(start, unvisited, outer, inner, grid, end, 0, i)
print(str(datetime.now() - startTime)[:-3])
# 422, NOTE CHANGED MK to RY TO REMOVE 2nd PAIR WHEN SORTING
