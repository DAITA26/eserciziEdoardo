massimo = int(input("Quale numero scegli? ").strip())


def stampa(parametro):
    print(parametro)

for n in range(1, massimo +1):
    if n % 15 == 0:
        stampa("Fizz and Buzz!!!")

    elif n % 3 == 0:
        stampa("Fizz!")
    elif n % 5 == 0:
        stampa("Buzz!")

    else:
        stampa(n)

