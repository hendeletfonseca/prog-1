competidor, papelComprado, folhasCompetidor = map(int, input().split())

if competidor * folhasCompetidor <= papelComprado:
    print('S')
else:
    print("N")

'''
    essa aqui nao tem misterio
    tu so tem que ver se tem folhas suficientes
    como voce recebe a quantidade de competidores e 
    quantas folhas cada um precisa
    multiplicando os 2 você chega em quantas folhas precisa ter
    se isso for menor ou igual a quantas vc têm, então dá p realizar a prova    
'''