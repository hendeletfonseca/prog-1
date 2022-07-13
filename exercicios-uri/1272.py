testes = int(input()) # quantas vezes vai executar o programa

for i in range(testes):
    codigo = '' # string vazia para adicionar as letras do codigo
    aux = True # True quando posso adicionar letra, False quando não
    texto = input()
    for letra in texto: # passo por cada char(letra) do texto
        if letra != ' ' and aux: # se letra for diferente de espaço e aux == True
            codigo += letra # concateno ao código a letra
            aux = False # torno aux == False para nao adicionar as proxima letra
        elif letra == ' ':
            aux = True
    print(codigo)
