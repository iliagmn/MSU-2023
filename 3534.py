n=int(input("Введите n: "))
k=int(input("Введите k: "))
a=[]
b=[]
a.append(n)
a.append(k)
a.append(n-k)


for i in a:
    f=1    
    s=1
    while s<=i:
        f=f*s
        s=s+1
        print(f)
    b.append(f)

print(b[0]/(b[1]*b[2]))
    
