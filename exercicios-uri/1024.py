def criptografar(x: str):
    new_word = ''
    descriptografado = ''
    a = 0
    for letra in x:
        if 65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122:
            letra = chr(ord(letra) + 3)
        new_word += letra
    new_word = new_word[::-1]
    for letra in new_word:
        if a >= len(new_word) // 2:
            letra = chr(ord(letra) - 1)
        a += 1
        descriptografado += letra

    return descriptografado


n = int(input())

for i in range(n):
    txt = str(input())
    print(criptografar(txt))
