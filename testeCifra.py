from cifraDeCesar import criptografa, descriptografa

loop = True

while(loop):
    print("Seja bem vindo ao cesar cifras!!!")
    print("Qual operação deseja realizar?")

    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair")

    escolha = int(input("Escolha: "))
    print()

    if (escolha == 1):
        frase = input("Insira a frase a ser criptograda: ")
        cifra = input("Insira a chave da cifra: ")
        print()
        criptografa(frase,cifra)
    elif (escolha == 2):
        frase = input("Insira a frase a ser descriptograda: ")
        cifra = input("Insira a chave da cifra: ")
        print()
        descriptografa(frase,cifra)
    elif (escolha == 3):
        loop = False
    else:
        print("escolha invalida")
    
    print()





