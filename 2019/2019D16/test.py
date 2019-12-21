'''

try:
    from datetime import datetime
    startTime = datetime.now()

    import re
    from collections import deque, Counter, defaultdict
    from itertools import permutations, combinations, count, product
    from operator import *
    import math

    filepath = 'input.txt'
    #filepath = 'test.txt'

    with open(filepath, 'r') as f:
        for line in f.readlines():
            input_signal = line.strip()
    base_pattern = [0, 1, 0, -1]

    offset = int(input_signal[:8])
    #input_signal = '12345678'

    signal = [int(i) for i in input_signal] * 10000

    phases = 1
    multiplication = []
    l = len(signal)
    print(1)
    startTime = datetime.now()
    for i in range(1, l+1):
        a = []
        for v in base_pattern:
            a = a + [v]*i
        a = a * math.ceil(l/(len(a)-1))
        a = a[1:l+1]
        multiplication.append(a)
    print(str(datetime.now() - startTime)[:-3])
    startTime = datetime.now()
    for i in range(phases):
        new_signal = ''
        for n, pos in enumerate(multiplication):
            val = str(sum(a*b for a,b in zip(signal,pos)))[-1]
            #print(str(sum(a*b for a,b in zip(signal,pos))))
            new_signal = new_signal + val
            #print(n)

        signal = [int(i) for i in new_signal]
        #print('main', i)
        #print(signal)

    print(''.join(str(i) for i in signal)[:8])
    print(''.join(str(i) for i in signal)[offset:offset+8])
    print(str(datetime.now() - startTime)[:-3])

except Exception:
    pass

print()

'''
#########################################################################################################3


'''

try:
    from datetime import datetime
    startTime = datetime.now()

    import re
    from collections import deque, Counter, defaultdict
    from itertools import permutations, combinations, count, product
    from operator import *
    import math

    filepath = 'input.txt'
    #filepath = 'test.txt'
    #input_signal = '12345678'

    with open(filepath, 'r') as f:
        for line in f.readlines():
            input_signal = line.strip()
    #print(input_signal)

    offset = int(input_signal[:8])
    #print(offset)
    base_pattern = [0, 1, 0, -1]

    signal = [int(i) for i in input_signal] * 10000

    phases = 1
    multiplication = []
    l = len(signal)
    print(2)
    startTime = datetime.now()

    for i in range(1, l+1):
        a = []
        for v in base_pattern:
            a = a + [v]*i
        a = a * math.ceil(l/(len(a)-1))
        a = a[1:l+1]
        multiplication.append(a)

        #print(i)

    #print('ready')

    
    for i in multiplication:
        print(i)

    print(str(datetime.now() - startTime)[:-3])
    startTime = datetime.now()

    for i in range(phases):
        new_signal = ''
        for n, pos in enumerate(multiplication):
            val = str(sum(a*b for a,b in zip(signal,pos)))[-1]
            new_signal = new_signal + val
            #print(n)

        signal = [int(i) for i in new_signal]
        #print(i)
        #print(signal)

    print(''.join(str(i) for i in signal)[:8])
    print(''.join(str(i) for i in signal)[offset:offset+8])

    print(str(datetime.now() - startTime)[:-3])

except Exception:
    pass
print()

'''


##########################################################################################################
try:
    from datetime import datetime
    startTime = datetime.now()

    import re
    from collections import deque, Counter, defaultdict
    from itertools import permutations, combinations, count, product
    from operator import *
    import math

    filepath = 'input.txt'
    #filepath = 'test.txt'


    with open(filepath, 'r') as f:
        for line in f.readlines():
            input_signal = line.strip()
    #print(input_signal)
    base_pattern = [0, 1, 0, -1]

    #input_signal = '12345678'

    signal = [int(i) for i in input_signal] * 10000 
    offset = int(input_signal[:8])
    #print(offset)

    phases = 1
    multiplication = []
    l = len(signal)

    '''for i in range(1, l+1):
        a = []
        for v in base_pattern:A
            a = a + [v]*i
        a = a * math.ceil(l/(len(a)-1))
        a = a[1:l+1]
        multiplication.append(a)

    for i in multiplication:
        print(i)'''
    print(3)

    for phase in range(phases):
        new_signal = ''
        for s in range(1, l+1):
            digit_sum = 0
            for n, i in enumerate(signal):
                if (s-1) > n:
                    continue

                multiplication = ((n+1)//s)%4
                digit_sum += i * base_pattern[multiplication]
                #print((s-1) > n, i * base_pattern[multiplication])   
                #if s > n:
                #    print(i * base_pattern[multiplication])
            #print()
            #val = str(sum(a*b for a,b in zip(signal,pos)))[-1]
            val = str(digit_sum)[-1]
            new_signal = new_signal + val
            #print(phase, s)
        signal = [int(i) for i in new_signal]
        #print(phase)
        #print(signal)

    print(''.join(str(i) for i in signal)[:8])
    print(''.join(str(i) for i in signal)[offset:offset+8])

    print(str(datetime.now() - startTime)[:-3])
except Exception:
    pass
print()

######################################################################################################################

try:
    from datetime import datetime
    startTime = datetime.now()

    import re
    from collections import deque, Counter, defaultdict
    from itertools import permutations, combinations, count, product
    from operator import *
    import math

    filepath = 'input.txt'
    #filepath = 'test.txt'


    with open(filepath, 'r') as f:
        for line in f.readlines():
            input_signal = line.strip()
    #print(input_signal)
    base_pattern = [0, 1, 0, -1]

    #input_signal = '12345678'

    signal = [int(i) for i in input_signal] * 10000
    offset = int(input_signal[:8])
    #print(offset)

    phases = 1
    multiplication = []
    l = len(signal)

    '''for i in range(1, l+1):
        a = []
        for v in base_pattern:
            a = a + [v]*i
        a = a * math.ceil(l/(len(a)-1))
        a = a[1:l+1]
        multiplication.append(a)

    for i in multiplication:
        print(i)'''
    print(4)
    startTime = datetime.now()

    for phase in range(phases):
        new_signal = ''
        for s in range(1, l+1):
            digit_sum = 0
            for n, i in enumerate(signal):
                if (s-1) > n:
                    continue

                multiplication = ((n+1)//s)%4
                digit_sum += i * base_pattern[multiplication]
                #print((s-1) > n, i * base_pattern[multiplication])   
                #if s > n:
                #    print(i * base_pattern[multiplication])
            #print()
            #val = str(sum(a*b for a,b in zip(signal,pos)))[-1]
            val = str(digit_sum)[-1]
            new_signal = new_signal + val
            #print(phase, s)
        signal = [int(i) for i in new_signal]
        #print(phase)
        #print(signal)

    print(''.join(str(i) for i in signal)[:8])
    print(''.join(str(i) for i in signal)[offset:offset+8])

    print(str(datetime.now() - startTime)[:-3])

except Exception:
    pass
print()


##################################################################################################################
try:
    from datetime import datetime
    startTime = datetime.now()

    import re
    from collections import deque, Counter, defaultdict
    from itertools import permutations, combinations, count, product
    from operator import *
    import math

    filepath = 'input.txt'
    #filepath = 'test.txt'

    with open(filepath, 'r') as f:
        for line in f.readlines():
            input_signal = line.strip()
    #print(input_signal)
    base_pattern = [0, 1, 0, -1]

    #input_signal = '12345678'
    offset = int(input_signal[:8])
    #print(offset)

    signal = [int(i) for i in input_signal] * 10000

    phases = 1
    multiplication = []
    l = len(signal)
    #print(l)
    #l = 20
    #l = 650
    '''
    for i in range(1, l+1):
        a = []
        for v in base_pattern:
            a = a + [v]*i
        a = a * math.ceil(l/(len(a)-1))
        a = a[1:l+1]
        multiplication.append(a)

    print('muli')'''
    #for n, i in enumerate(multiplication):
    #    print(n, str((n)/l)[:4], i)

    # over 1/3, then over half
    startTime = datetime.now()

    def p1(n):
        if 3*n+2 < l: # below about a third
            digit = 0
            for v in range(n+1):
                digit += sum(signal[n+v::(n+1)*4])
                #print('plus', signal[n+v::(n+1)*4])
                digit -= sum(signal[n+v+(n+1)*2::(n+1)*4])
                #print('minus', signal[n+v+(n+1)*2::(n+1)*4])
            #print('first', digit)

        elif 2*n+1 < l:
            #print('second', sum(signal[n:2*n+1]))
            digit = sum(signal[n:2*n+1])
        else:
            #print('third', sum(signal[n:]))
            digit = sum(signal[n:])

        return int(str(digit)[-1])

    print(5)
    #print('starting')
    for i in range(phases):
        new_signal = ''
        #for n, pos in enumerate(multiplication):
        #for n in range(l):
        signal = [p1(n) for n in range(l)]
        #print(''.join(str(i) for i in signal))
        #print('main', i, ''.join(str(i) for i in signal))
        #print(signal)'''

    print('p1 ANSWER', ''.join(str(i) for i in signal)[:8])
    print(''.join(str(i) for i in signal)[offset:offset+8])
    print(str(datetime.now() - startTime)[:-3])

except Exception:
    pass

