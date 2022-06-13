

alfab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabetoModificado = []

def modifica_alfabeto(cifra):
    index = alfab.index(cifra.upper())

    for x in alfab:
        if index >= len(alfab):
            index = 0
            alfabetoModificado.append(alfab[index])
        else:
            alfabetoModificado.append(alfab[index])
        index += 1

def criptografa(frase, cifra):

    modifica_alfabeto(cifra)

    criptografada = ""
    for i in frase.upper():
        if (i in alfab):
            criptografada += alfabetoModificado[alfab.index(i)]
        else:
            criptografada += i
    print("frase criptograda: ",criptografada)
    return criptografada

def descriptografa(frase, cifra):

    modifica_alfabeto(cifra)

    descriptografada = ""
    for i in frase.upper():
        
        if (i in alfab):
            descriptografada += alfab[alfabetoModificado.index(i)]
        else:
            descriptografada += i
    print("frase descriptograda: ",descriptografada)
    return descriptografada



