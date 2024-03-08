
'''
Avengers=[]
Revengers=[]
Norbu=int(input("Enter the number of elements in Avengers: "))
for i in range(Norbu):
    Electro=input("Enter the element "+str((i+1))+": ")
    Avengers.append(Electro)
print("\n")

Nor=int(input("Enter the number of elements in Revengers: "))
for i in range(Nor):
    Elec=input("Enter the element "+str((i+1))+": ")
    Revengers.append(Elec)
print("\n")

Rag=[]
for i in Avengers:
    if i not in Revengers:
        Rag.append(i)

Ragnarok=Rag+Revengers

print(Avengers)
print(Revengers)
print(Rag)
print(Ragnarok)


Avengers=()
Revengers=()
Norbu=int(input("Enter the number of elements in Avengers: "))
for i in range(Norbu):
    Electro=input("Enter the element "+str((i+1))+": ")
    Avengers= Avengers+(Electro,)
print("\n")

Nor=int(input("Enter the number of elements in Revengers: "))
for i in range(Nor):
    Elec=input("Enter the element "+str((i+1))+": ")
    Revengers=Revengers+(Elec,)
print("\n")

Rag=()
for i in Avengers:
    if i not in Revengers:
        Rag=Rag+(i,)

Ragnarok=Rag+Revengers
CivilWar=Avengers+Revengers

print(Avengers)
print(Revengers)
print(CivilWar)
print(Rag)
print(Ragnarok)

Avengers={}
Revengers={}
Norbu=int(input("Enter the number of elements in Avengers: "))
for i in range(Norbu):
    Electro=input("Enter the element "+str((i+1))+": ")
    Avengers[i]=Electro
print("\n")

Nor=int(input("Enter the number of elements in Revengers: "))
for i in range(Norbu,(Norbu+Nor)):
    Elec=input("Enter the element "+str((i+1))+": ")
    Revengers[i]=Elec
print("\n")

aval=Avengers.values()
rval=Revengers.values()
Rag={}

for i in aval:
    if i not in rval:
        Rag[i] = i

Rag.update(Revengers)

print(Rag.values())
print(Avengers.values())
print(Revengers.values())'''



Avengers=set()
Revengers=set()

Norbu=int(input("Enter the number of elements in Avengers: "))
for i in range(Norbu):
    Electro=input("Enter the element "+str((i+1))+": ")
    Avengers.add(Electro)
print("\n")

Nor=int(input("Enter the number of elements in Revengers: "))
for i in range(Nor):
    Elec=input("Enter the element "+str((i+1))+": ")
    Revengers.add(Elec)
print("\n")

Ragnarok=Avengers.union(Revengers)

print(Avengers)
print(Revengers)
print(Ragnarok)










