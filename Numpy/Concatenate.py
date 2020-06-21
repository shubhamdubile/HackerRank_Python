import numpy
N,M,P = map (int, input().split())
first_array=numpy.array([input().split() for _ in range (N)],int)
second_array=numpy.array([input().split() for _ in range (M)],int)
a=numpy.concatenate((first_array,second_array))
print(a)



