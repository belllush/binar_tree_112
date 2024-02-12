# Функция для поиска пути
def way(input_string, index, arr, summa):
    if index < len(input_string):
        if input_string[index] is not None:
            arr.append(input_string[index])
            if sum(arr) == summa and way(input_string, index * 2 + 1, arr.copy(), summa) and way(input_string, index * 2 + 2, arr.copy(), summa):
                print('->'.join([str(elem) for elem in arr]))
                return False
            else:
                way(input_string, index * 2 + 1, arr.copy(), summa)
                way(input_string, index * 2 + 2, arr.copy(), summa)
                return False
    #Возвращаем True, если индекс выходит за пределы списка или текущий узел None
        else:
            return True
    else:
        return True


print("Введите строку с значениями узлов:")
s = input()
print("Введите сумму:")
n = int(input())
nodes = []
for el in s.split(','):
    if el == '':
        nodes.append(None)
    else:
        nodes.append(int(el))

#если какой-то элемент отсутсвуют, то отсутстуют и его дочерние элементы
next_uzel = 1
perehod_na_next_sloy = 1
for i in range(len(nodes)):
    if i == next_uzel:
        perehod_na_next_sloy *= 2
        next_uzel += perehod_na_next_sloy
    if nodes[i] is None and i * 2 + 1 >= next_uzel and len(nodes) > next_uzel:
        nodes.insert(i * 2 + 1, None)
        nodes.insert(i * 2 + 2, None)

way(nodes, 0, [], n)



#5,4,8,11,,13,4,7,2,,,,1