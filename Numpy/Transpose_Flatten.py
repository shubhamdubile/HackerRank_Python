import numpy
N,M = map(int,input().split())
list = []
for _ in range (0,N):
    l=input().split()
    list.append([i for i in l])
arr1=numpy.array(list,int)
print(numpy.transpose(arr1))
print(arr1.flatten())

