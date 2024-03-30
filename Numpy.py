
from numpy import *

a=array([[1,2,-3,4,-5,-6,7],
         [8,-9,10,11,-12,13,14]])
print(a.ndim)   #Dimension of matrix
print(a.shape)  #Shape of matrix, structure like (rows, columns)
print(a.dtype)  #Type of matrix like int16, int32 etc
print(a.itemsize) #Bytes taken up by one element
print(a.size)   #Total no of elements in the array
print(a.nbytes) #Total no of bytes taken by full array
print(a[0,1])   #Accessing Matrix Elements
print(a[1,:])   #Accessing Matrix Rows
print(a[:,-2])  #Accessing Matrix Columns


print(a[0,1:-1:2],end="\n\n")
print(f'Zero\'s Matrix: \n{zeros((2,3))}\n')
print(f'One\'s Matrix: \n{ones((2,3))}\n')
print(f'Desired No\'s Matrix: \n{full((2,3),30)}\n')
print(f'Desired No\'s Matrix in structure of \'a\': \n{full_like(a,30)}\n')
print(f'Desired No\'s Matrix in structure of \'a\' but another way: \n{full(a.shape,30)}\n')
print(f'Random Decimal No\'s Matrix: \n{random.rand(2,3)}\n')
print(f'Random Decimal No\'s Matrix in structure of \'a\': \n{random.random_sample(a.shape)}\n')
print(f'Random Integer No\'s Matrix: \n{random.randint(7,31, size=(2,5))}\n')
print(f'Identity Matrix: \n{identity(5)}\n')
print(f'Repeated Array: \n{repeat(a,2,axis=0)}\n')

#Pattern Printing

# 1,1,1,1,1
# 1,0,0,0,1
# 1,0,9,0,1
# 1,0,0,0,1
# 1,1,1,1,1

result= ones((5,5))
mid= zeros((3,3))
mid[1][1]=9
result[1:4, 1:4]=mid
print(result, end="\n\n")


#Maths on Matrices
A=array([1,2,3,4,5])
B=array([1,3,5,7,9])
print(f'Matrix Addition: {A+29}')
print(f'Matrix Subtraction: {A-9}')
print(f'Matrix Multiplication: {A*9}')
print(f'Matrix Division: {A/2}')
print(f'Matrix Exponentiation: {A**2}')
print(f'Matrix Plus Matrix: {A+B}')
print(f'Matrix Sine: {sin(A)}')
print(f'Matrix Cosine: {cos(A)}')

alpha=ones((2,3))
beta=full((3,2), 3)
print(f'Matrix Multiply Matrix: \n{matmul(alpha, beta)}')
print(f'Matrix Determinant: {linalg.det(identity(2))}')

#Statistics
s=array([[1,2,3], [4,5,6]])
print(s)
print(f'Minimum value in s: {s.min()}')
print(f'Minimum value in s by row: {s.min(axis=0)}')
print(f'Minimum value in s by column: {s.min(axis=1)}')
print(f'Maximum value in s: {s.max()}')
print(f'Maximum value in s by row: {s.max(axis=0)}')
print(f'Maximum value in s by column: {s.max(axis=1)}')
print(f'Sum of values in s: {s.sum()}')

#Reorganizing
print(f'Reshaped s: \n{s.reshape((3,2))}')
print(f'Verically Stacked: \n{vstack([A,B])}')
print(f'Horizontally Stacked: \n{hstack([A,B])}')

#Miscellaneous
da=genfromtxt('../../Python 1/a.txt', delimiter=',').astype('int32')
print(f'Data from a.txt: \n{da}')
print(f'Boolean Data from a.txt: \n{da>29}')
print(f'List Indexing array A: \n{A[[2,3,1,4]]}')
print(f'Any function on array da: \n{any(da<31, axis=0)}')
print(f'All function on array da: \n{all(da<31, axis=0)}')

# Question
qsnmatrix=array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(f'Question Matrix: \n{qsnmatrix}')
print(f' Question 1=> Access 11,12,16 and 17')
print(f' Question 2=> Access 2,8,14 and 20')
print(f' Question 3=> Access 4,5,24,25,29 and 30')

ans1=qsnmatrix[2:4,0:2]
ans2=qsnmatrix[[0,1,2,3],[1,2,3,4]]
ans3=qsnmatrix[[0,4,5],3:]

print(f'Answer 1: \n{ans1}')
print(f'Answer 2: \n{ans2}')
print(f'Answer 3: \n{ans3}')