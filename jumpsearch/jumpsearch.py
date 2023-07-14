import csv
import math

def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)]<x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1


with open('E:\\python\\trabalhofinal\\notas.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    data = list(reader)
    data = [int(i[0]) for i in data]

x = 22032 
index = jump_search(data, x)

if index != -1:
    print("Estudante", x, "está na posição", "%.0f" %index)
else:
    print("Estudante", x, "não está no array")
