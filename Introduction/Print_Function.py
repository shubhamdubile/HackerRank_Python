Solution:-
n = int(input())
for _ in range (1,n+1):
    print(_,end='')
    
    
    
Another Solution:-
if __name__ == '__main__':
    n = int(input())
    list=[]
    for i in range(1,n+1):
        list.append(i)
    print(''.join(str(e) for e in list))    
    
