n=int(input("Введите n: "))

q=1
f=n
while f//10>=1:
    f=f//10
    q=q+1

for i in range (10**q, 10**(q-1)-1, -1 ):
    if i%2==1:
        print(i, end = " ")
    else:
        continue