
"""
#Lambda
tplus=lambda x:x+10
print(tplus(10))

mult=lambda x,y:x*y
print(mult(5,6))

points=[(3,4),(71,5),(45,5),(6,99),(23,55)]

sumsort=sorted(points, key=lambda x:x[0]+x[1])
sortpoints=sorted(points, key=lambda x:x[1])
sopo=sorted(points)

print(points)
print(sopo)
print(sortpoints)
print(sumsort)

#Map(func, seq)
a=[1,2,3,4,5,6,7,8]
b=map(lambda x:x*2,a)
print(list(b))

#List comprehension
c=[x*2 for x in a]
print(c)

#Filter(func, seq)
d=filter(lambda x:x%2==0,a)
print(list(d))
dlc=[x for x in a if x%2==0]
print(dlc)

#Reduce(func, seq)
from functools import reduce
e=reduce(lambda x,y:x+y, a)
print(e)

#List Comprehension
nums=[23,54,66,5,7,433,53,565,973,264]
even=[x for x in nums if x%2==0]
print(even)

fruits=["apple","banana","guava","strawberry"]
fruits=[i.title() for i in fruits]
print(fruits)

bits=[True,True,False,True,False,True,True,False,True,False,True,False]
print(bits)
bits=[1 if b==True else 0 for b in bits]
print(bits)

superman="IAmTejaswaniSharma"
superman="".join([i if i.islower() else " "+i for i in superman])
print(superman[1:])

#Dictionary Comprehension
name=["Bruce","Peter","Tony","Clark"]
hero=["Batman","Spiderman","Iron Man","Superman"]
profession={key:value for key,value in zip(name,hero)}
print(profession)

proff={name[i]:hero[i] for i in range(len(name))}
print(proff)

work={"Spider":"Photographer","Bat":"Philanthropist","Wonder Wo":"Archaeologist"}
work={(key+"man" if key!="Bat" else "Superman" ):value if key!="Bat" else "Journalist" for (key,value) in work.items()}
print(work)

from random import choices
bases=["A","G","C","T"]
strand=choices(bases,k=12)
dna={key:[value, "T" if value=="A" else "C" if value=="G" else "A" if value=="T" else "G"] for key,value in enumerate(strand)}
print(dna)

from string import printable

details=["Id","Username","Password"]
users=["Nitin","Preeti"]
data=[{detail:(i+1 if detail=="Id" else users[i] if detail=="Username" else "".join(choices(printable,k=8))) for detail in details}for i in range(len(users))]
print(data)"""