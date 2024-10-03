def main():

    acc = 0
    palavra = str(input("Escreva a frase: "))
    for i in palavra:
        
        if i == 'a' or i == 'A':
            acc += 1
    if acc > 0 :
        print(f"A frase tem a letra A e ela ocorre : {acc} ")
    else:
        print("A frase nao tem a letra A")
    return 0

main()