# subprograms
def nearest_and_furthest_point(file, x, y, ignore_line):
    pos = 0
    nearest = []
    furthest = [0, x, y]
    data = open(file, 'r')
    for line in data:
        if pos != ignore_line:
            x1, y1 = map(int, line.split())
            distance = points_distance(x, y, x1, y1)
            if nearest == []:
                nearest.append(distance)
                nearest.append(x1)
                nearest.append(y1)
            elif distance < nearest[0]:
                nearest[0], nearest[1], nearest[2] = distance, x1, y1
            if distance > furthest[0]:
                furthest[0], furthest[1], furthest[2] = distance, x1, y1
        pos += 1
    data.close()
    return nearest, furthest


def points_distance(x, y, x2, y2):
    distance = ((x-x2)**2 + (y-y2)**2)**0.5
    return distance


# main program
count = 0
file_name = input('Digite o nome do arquivo: ')
file_data = open(file_name, 'r')
for point in file_data:
    px, py = map(int, point.split())
    nearest_point, furthest_point = nearest_and_furthest_point(file_name, px, py, count)
    print(f'Ponto {count + 1}: ({px}, {py})')
    print(f'Ponto mais próximo: ({nearest_point[1]}, {nearest_point[2]})')
    print(f'Ponto mais distante: ({furthest_point[1]}, {furthest_point[2]})')
    print()
    count += 1
file_data.close()
if count == 0:
    print('Arquivo sem pontos!!!')
