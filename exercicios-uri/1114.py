# https://www.beecrowd.com.br/judge/pt/problems/view/1114

senha = input()
while senha != "2002":
    print("Senha Invalida")
    senha = input()
if senha == "2002":
    print("Acesso Permitido")
