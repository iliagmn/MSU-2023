A=int(input("Введите число А: "))
B=int(input("Введите число B: "))

if A>B:
    while A>=B:
        print(A, end = " ") 
        A=A-1
elif A<B:
    while A<=B:
        print(A, end = " ")
        A=A+1
else:
    print(A)

    т