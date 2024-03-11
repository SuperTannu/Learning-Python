
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

a=[1,2,3,4]
b=[5,6,7]
pro=itertools.product(a,b)
print(list(pro))
