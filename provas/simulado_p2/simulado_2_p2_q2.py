def verify(id, min_coef, max_coef, min_workload, max_workload):
    total_workload = 0
    total_coef = 0
    real_workload = 0
    student_data = open(id + '.txt', 'r', encoding='utf-8')
    for line in student_data:
        if '#' in line:
            name, semester, workload, grade = line.split('#')
            if float(grade) >= 6:
                total_workload += int(workload)
            total_coef += float(grade) * int(workload)
            real_workload += int(workload)
    total_coef = total_coef / real_workload
    student_data.close()
    if min_coef < total_coef < max_coef and min_workload < total_workload < max_workload:
        print_datas(id, total_workload, total_coef)
    return None


def print_datas(id, workload, coef):
    nome, curso = '', ''
    aux = 0
    student_data = open(id + '.txt', 'r', encoding='utf-8')
    for line in student_data:
        if '#' not in line:
            if aux == 0:
                curso = line.strip('\n')
                aux += 1
            elif aux == 1:
                nome = line.strip('\n')
                aux += 1
    student_data.close()
    print(f'Nome: {nome}')
    print(f'Curso: {curso}')
    print(f'Carga Horária Efetiva: {workload}')
    print(f'Coeficiente de Rendimento: {coef:.2f}')
    print()
    return None


file_name = input('alunos: ')
coef_min, coef_max = map(float, input('3.5 9.2').split())
workload_min, workload_max = map(int, input('100 800').split())
data = open(file_name + '.txt', 'r', encoding='utf-8')
for line in data:
    verify(line.strip('\n'), coef_min, coef_max, workload_min, workload_max)
data.close()
