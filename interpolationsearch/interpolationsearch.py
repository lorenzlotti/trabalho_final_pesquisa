import csv

def interpolation_search(arr, x):
    low = 0
    high = (len(arr) - 1)

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x :
                return low
            return -1

        pos = low + int(((float(high - low) / ( arr[high] - arr[low])) * ( x - arr[low])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

with open('E:\\python\\trabalhofinal\\notas.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    data = list(reader)
    data = sorted([int(i[0]) for i in data])

x = 22045  # The student ID we're searching for
index = interpolation_search(data, x)

if index != -1:
    print("Estudante", x, "está na posição", "%.0f" %index)
else:
    print("Estudante", x, "não está no array")
