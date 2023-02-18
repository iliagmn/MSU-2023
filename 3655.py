i=100000000000000000
a=[]
while i!=0:
    i=int(input())

    if i<0: exit()
    
    c=0
    n=len(a)
    if n==0: a.append(i)
    for k in range(n):
        if i!=a[k]:
            c=c+1
            if c==n: a.append(i)
        else:
            continue
    
a_new=sorted(a)
print(a_new[2])
    
        