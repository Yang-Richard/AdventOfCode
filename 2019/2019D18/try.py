import numpy, sys, copy
from datetime import datetime
startTime = datetime.now()
grid = numpy.zeros((0, 0))

ADJACENTS = {(0, -1), (0, 1), (-1, 0), (1, 0)}

filepath = 'input.txt'
#filepath = 'test.txt'
    
def pathfind(start, end, unvisited, doors, keys):
    t = datetime.now() 
    visited = {}
    #print(tuple(start))
    paths = {tuple(start): ''}
    while unvisited:
        current_node = list(unvisited.keys())[0]
        current_val = unvisited[list(unvisited.keys())[0]]
        for key, val in unvisited.items():
            if val < current_val:
                current_node = key
                current_val = val
        #if current_node == end:
        #    print(datetime.now()-t)
        #    return current_val
        end = True
        for adjacent in ADJACENTS:
            x, y = current_node[0] + adjacent[0], current_node[1] + adjacent[1]

            for key, val in unvisited.items():
                if key == (x, y) and val > current_val + 1:
                    unvisited[key] = current_val + 1
                    
                    if (x, y) in doors.keys():
                        paths[x, y] = paths[current_node] + doors[x, y]
                    elif (x, y) in keys.keys():
                        paths[x, y] = paths[current_node] + keys[x, y]
                    else:
                        paths[x, y] = paths[current_node]
                    
                    #print('DOING')
                    end = False
                    break
                    
        #print(current_node, end)
                    
        if not end:
            del paths[current_node]
            
        visited[current_node] = unvisited.pop(current_node)
        
    #print(str(datetime.now() - startTime)[:-3])
    #for key, path in paths.items():
    #   if path != '':
    #       print(key, path)
    #print(paths)
    locks = set(paths.values())
    #for lock in locks:
    #    print(lock)
        
    sorted_locks = sorted(list(locks))
    
    for lock in sorted_locks[:]:
        for other_lock in sorted_locks[:]:
            if lock != other_lock and lock in other_lock:
                sorted_locks.remove(lock)
                #print('removing', lock)
                break
    
    return sorted_locks
    
doors = {}
keys = {}
unvisited = {}
start = None
y = 0
with open(filepath, 'r') as f:
    for line in f.readlines():
        for x, n in enumerate(line.strip()):
            if n == '@':
                unvisited[x, y] = 0
                start = [x, y]
            elif n == '.':
                unvisited[x, y] = float('inf')
            elif n.isalpha():
                if n.islower():
                    keys[x, y] = n
                elif n.isupper():
                    doors[x, y] = n
                else:
                    print('sad elf')
                unvisited[x, y] = float('inf')
            else:
                pass
        y += 1
        

# get all the possible moves
#    includes  getting keys
#     includes using keys to open doors
#    pathfind from each spot to each spot


#print(unvisited)
#print(doors)
#print(keys)

#print(len(doors.keys()))
#print(len(keys.keys()))

sorted_paths = pathfind(start, None, unvisited, doors, keys)

for n, paths in enumerate(sorted_paths):
    print(str(n).zfill(2), paths)
#print(str(datetime.now() - startTime)[:-3])

import itertools
def find_paths(sorted_paths, t, available_keys = []):
    # print('recursion lvel', t, sorted_paths)
    if t == 9:
        return ' '
    options = set()
    for n, path in enumerate(sorted_paths[:]):
        if path[0].islower():
            options.add(path[0])
            #sorted_paths[n] = sorted_paths[n][1:]
        
        if path[0].lower() in available_keys:
            options.add(path[0])
            #sorted_paths[n] = sorted_paths[n][1:]
            
    sorted_paths = [path for path in sorted_paths if path != '']
            
    options = list(options) 
    #available_keys = available_keys + [i for i in options if i.islower()]
    '''
    if len(sorted_paths) != 0 :#and len(options) != 1:
        next_options = find_paths(sorted_paths, available_keys)
        
        options = [i for i in itertools.product(options, next_options)]
        #for option in options:
        #    option = option + '''
    #print('current options', options)
    #print(options)
    #if options == ['o', 'a', 'd', 'n', 'i']:
    #    options = ['a']
        
    
    output_options = set()
    for n, option in enumerate(options):
        new_sorted_paths = sorted_paths[:]
        new_available_keys = available_keys[:]
        
        if option.islower():
            new_available_keys.append(option)
        
        for n in range(len(new_sorted_paths)):
            if option in new_sorted_paths[n]:
                new_sorted_paths[n] = new_sorted_paths[n][1:]
                
        new_sorted_paths = [path for path in new_sorted_paths if path != '']
        #print('currently using option', option)
        #print('new sorted for current option', new_sorted_paths, new_available_keys)
        if len(new_sorted_paths) != 0:
            #print('recursing')
            next_options = find_paths(new_sorted_paths, t+1,  new_available_keys)
            #options[n] = [i for i in itertools.product(option, next_options)]
            #print('next options', next_options)
            for v in next_options:
                output_options.add(option + v)
                #print('possibility', option + v)
        else:
            output_options = (option)
        
    return output_options
    
    

#print(find_paths(['a', 'abcdefghi', 'abcdefgz'],0))
print('final', len(find_paths(sorted_paths,0)))