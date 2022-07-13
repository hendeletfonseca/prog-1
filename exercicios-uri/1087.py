x1, y1, x2, y2 = map(int, input().split())

while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0: # enquanto os valores forem diferente de 0 continua no laço
    if x1 == x2 and y1 == y2: # verifica se a coordenada inicial igual a coordenada final
        print(0)
    elif x1 == x2 or y1 == y2: # verifica se o inicio e fim estão na mesma linha ou coluna
        print(1)
    elif (x1 + y1 == x2 + y2) or (x1 - y1 == x2 - y2): # verifica se estão na diagonal (só 1 movimento também)
        print(1)
    else:
        print(2)
    x1, y1, x2, y2 = map(int, input().split())