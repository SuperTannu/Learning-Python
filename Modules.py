
import collections
#Counter
sent="Programmer."
count=collections.Counter(sent)
print(count)

#Most common
moc=count.most_common(3)
print(moc)

#Elements
e=list(count.elements())
print(e)

#Named Tuple
Point=collections.namedtuple("Point","x,y")
p=Point(30,57)
print(p)

#Ordered Dict
D=collections.OrderedDict()
D[1]="Alpha"
D[2]="Beta"
print(D)

#Default Dict
d=collections.defaultdict(int)
d[1]=32
d[2]=44
print(d)
print(d[3])

#Deque
deq=collections.deque()
deq.append(2)
deq.appendleft(41)
deq.append(30)
deq.append(23)
print(deq)
deq.rotate()
print(deq)

import itertools

#Product
a=[1,2,3,4]
b=[5,6,7]
pro=itertools.product(a,b)
print(list(pro))

#Permutations and Combinations
perm=itertools.permutations(a,2)
combi=itertools.combinations(a,3)
combiwr=itertools.combinations_with_replacement(a,2)
print(list(perm))
print(list(combi))
print(list(combiwr))

#Accumulate
acc=itertools.accumulate(a)
print(a)
print(list(acc))

import operator
accu=itertools.accumulate(a, func=operator.mul)
print(list(accu))

#Groupby

def lt(x):
    return x<=3

gr=itertools.groupby(a, key=lt)
for key, value in gr:
    print(key,list(value))

#Infinite Operators
for i in itertools.count(5): #Count
    print(i)
    if i>29:
        break

for i in itertools.cycle(a): #Cycle
    print(i)
    break


rep=itertools.repeat(30,5) #Repeat
print(list(rep))

