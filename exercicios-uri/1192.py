# https://www.beecrowd.com.br/judge/pt/problems/view/1192

maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç']
minusculas = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
casosDeTeste = int(input())
for i in range(casosDeTeste):
    seqTemp = list(input())
    if seqTemp[0] == seqTemp[2]:
        print(f'{int(seqTemp[0])**2}')
    else:
        if seqTemp[1] in maiusculas:
            print(f'{int(seqTemp[2]) - int(seqTemp[0])}')
        else:
            print(f'{int(seqTemp[0]) + int(seqTemp[2])}')
