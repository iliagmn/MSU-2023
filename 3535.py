n=int(input("Введите число n: "))

a=[]
b=[]
s=1
for i in range (1, n+1):
    s = i*(i+1)
    b.append(s)
    y1 = str(i)
    a.append(y1)
    a.append('*')
    y2 = str(i+1)
    a.append(y2)
    a.append('+')
    
summ = sum(b)
summ_str = str(summ) 
   
st = ""
for word in a:
    st += str(word)
    
st=st[:-1]

summ2 = st+'='+summ_str
print(summ2)
print(summ2)
print(summ2)
print(summ2)
    
    

