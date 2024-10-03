def main():
    a1 = 0
    a2 = 1
    res = 0
    numero = int(input("Informe o numero: "))

    if numero == 0:
        print("O número está na sequência.")
        return
    elif numero == 1:
        print("O número está na sequência.")
        return

    while True:
        res = a1 + a2

        if res > numero: 
            print("O número não está na sequência.")
            break
        elif res == numero:
            print("O número está na sequência.")
            break

        a1 = a2 
        a2 = res

main()
