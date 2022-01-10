def print_file(txt, string):
    print(f'Pontos do arquivo {txt} {string}')
    datas = open(txt, 'r', encoding='utf-8')
    for line in datas:
        print(line.strip('\n'))
    datas.close()
    print()
    return None


def find_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def remove_points(txt, cx, cy, min_distance):
    from os import remove, rename
    datas = open(txt, 'r', encoding='utf-8')
    temp_file = open('temp_txt', 'a', encoding='utf-8')
    for line in datas:
        x1, y1 = map(int, line.strip('\n').split())
        if find_distance(x1, y1, cx, cy) > min_distance:
            temp_file.write(f'{x1} {y1}' + '\n')
    datas.close()
    temp_file.close()
    remove(txt)
    rename('temp_txt', txt)
    return None


file_name = input('ps')
x_center, y_center, radius = map(int, input('80 85 40').split())
print_file(file_name + '.txt', 'antes das remoções:')
remove_points(file_name + '.txt', x_center, y_center, radius)
print_file(file_name + '.txt', 'depois das eventuais remoções:')
