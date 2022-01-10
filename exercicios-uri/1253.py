# https://www.beecrowd.com.br/judge/pt/problems/view/1253

n = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n):
    texto = input().upper()     #.upper deixa todas maiusculas
    deslocamento = int(input())
    novo_texto = ''
    for letra in texto:
        posicao = alphabet.find(letra) - deslocamento #.find retorna a posição do caracter na string
        novo_texto += alphabet[posicao]
    print(novo_texto)
