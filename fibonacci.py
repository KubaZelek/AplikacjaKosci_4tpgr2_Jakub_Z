def fibonacci(n):
    a = 1
    b = 1
    if n<=0:
        print("Nie ma ciagu dla takiej liczby")
    else:
        for i in range(n):
            print(f"Kolejna liczba ciagu: {a}")
            b+=a
            print(f"Liczba b (wczesniejsze b+a): {b}")
            a = b-a
            print(f"Liczba a (b-a): {a}")
    return b
while True:
    liczba = int(input("Podaj liczbe do ciagu fibonacciego: "))
    fibonacci(liczba)
        
        