digito, numero = input().split()
while digito != '0' and numero != '0': # verifico se D e N são diferentes de 0, se forem continua no loop

    valorCorrigido = '0'
    # crio uma string com valor 0 (nao pode ser vazia pq quando nao tiver valor nao vou ter como converter em int)

    for i in numero: # passo em cada digito do numero e verifico se é diferente do digito a ser removido
        if i != digito:
            valorCorrigido += i # concateno o valor a str(valorCorrigido) se for diferente do digito

    valorCorrigido = int(valorCorrigido) # converto a str em int (para remover 0's a esquerda e nao printar nada como: 000007 e sim apenas 7)

    print(valorCorrigido)

    digito, numero = input().split() # recebo novamente os valores para verificar se sigo no loop
