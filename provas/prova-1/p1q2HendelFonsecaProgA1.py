def calcularRaio(centro, pontos):
    maiorDistancia = 0
    for i in range(len(pontos)):
        distancia = ((float(pontos[i][0]) - float(centro[0]))**2 + (float(pontos[i][1]) - float(centro[1]))**2)**0.5
        if distancia > maiorDistancia:
            maiorDistancia = distancia
    return maiorDistancia


qtdPontos = 0
todosPontos = []
xs = 0
ys = 0
ponto = input().split()
while ponto != []:
    qtdPontos += 1
    xs += int(ponto[0])
    ys += int(ponto[1])
    todosPontos.append(ponto)
    ponto = input().split()
if todosPontos != []:
    CentroGeo = f'({xs/qtdPontos:.2f}, {ys/qtdPontos:.2f})'
    raio = calcularRaio([xs/qtdPontos, ys/qtdPontos], todosPontos)
    print(f'Centro Geométrico: {CentroGeo} e Raio: {raio:.2f}')
if todosPontos == []:
    print('Nenhum Ponto Foi Lido!!!')

