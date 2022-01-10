"""
Alunos
3.5 9.2
100 800
"""
# Programa - P2Q2
# Subprogramas
def extrato(matAluno):
    dadosAluno = open(matAluno, "r", encoding="utf-8")
    cursoAl = dadosAluno.readline().strip("\n")
    nomeAl = dadosAluno.readline().strip("\n")
    totalHoras = 0
    fatoresDasDisciplinas = 0
    cHAl = 0
    for disciplina in dadosAluno:
        nmDis, semDis, cHDis, notaDis = disciplina.split("#")
        cHDis = int(cHDis)
        notaDis = float(notaDis)
        if notaDis >= 6.0:
            cHAl += cHDis
        totalHoras += cHDis
        fatoresDasDisciplinas += notaDis*cHDis
    dadosAluno.close()
    if totalHoras > 0:
        cRAl = fatoresDasDisciplinas/totalHoras
    else:
        cRAl = 0
    return nomeAl, cursoAl, cHAl, cRAl

def listaAlunosCReCH(nm, minCR, maxCR,cHMin, cHMax):
    dados = open(nm, "r")
    for matricula in dados:
        nome, curso, cHEfetiva, cR = extrato(matricula.strip("\n"))
        if minCR <= cR <= maxCR and cHMin <= cHEfetiva <= cHMax:
            print("Nome:", nome)
            print("Curso:", curso)
            print("Carga Horária Efetiva:", cHEfetiva)
            print("Coeficiente de Rendimento: %.2f"%cR)
            print()
    dados.close()
    return None

# Principal
nomeAlunosDoCurso = input()
minimoCR, maximoCR = map(float, input().split())
cargaHorariaMin, cargaHorariaMax = map(int, input().split())
listaAlunosCReCH(nomeAlunosDoCurso, minimoCR, maximoCR, cargaHorariaMin, cargaHorariaMax)