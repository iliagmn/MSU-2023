A=int(input("Введите число А: "))
B=int(input("Введите число B>=A: "))

if A>B:
    print("Числа не удовлетворяют условию!")
    quit()

while A<=B:
    print(A, end = " ")
    A=A+1
    