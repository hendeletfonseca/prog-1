# https://www.beecrowd.com.br/judge/pt/problems/view/1235

# SubPrograma
def criptografar(x):
    new_word = ''
    control = 0
    control_2 = 0
    temp = ''
    for letra in x:
        if control < len(x) // 2:
            control += 1
            temp = x[(len(x) // 2) - control]
        else:
            control_2 += 1
            temp = x[len(x) - control_2]
        new_word += temp
    return new_word


# principal
n = int(input())
for i in range(n):
    txt = input()
    print(criptografar(txt))
