'''
# sys module
import sys
print(sys.path)
print(sys.version)
print('start')
sys.exit()  # here the program is going to exit not go for next line
print('end')

# platform
import platform 
print(platform.system())
print(platform.release())
print(platform.processor())


# mathemetacial functions
import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow)
print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.99999))
print(math.floor(12.000001))
print(math.floor(12.3))
print(math.floor(12.6))
print(math.floor(12.99999))
print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))


# RANDOM MODULE
import random
random.seed(10)
print(random.randint(1,10))
print(random.randint(10,100))
print(random.random())
print(random.uniform(1,10))
l=['r','s','p']
print(random.choice(l))
print(random.choices(l,k=2))
random.shuffle(l)
print(l)


# counter
from collections import Counter,defaultdict,deque
s='python programming'
m='this is this that is that that is this'.split()
l=[1,1,1,1,2,2,3,3,2,3,5,24,34,54,3,4,5,5,]
print(Counter(s))
print(Counter(m))
print(Counter(l))

# default dict
d= defaultdict(int)
s='python programming'
for i in s:
    d[i]+=1
print(d)    

#deque
l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)

l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.append(30)
l.append(50)
l.append(70)
l.pop()
print(l)

'''

# permutations and combinations
from itertools import combinations,permutations
res1=list(combinations("abs",2))
res2=list(permutations("abs",2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
