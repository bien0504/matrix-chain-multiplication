import random

with open('data.txt', 'r') as file:
    data = file.read().split(',')
    data = [int(num) for num in data]
    n = len(data)

A = [[data[i], data[i+1]] for i in range(0, n-1)]

print("A:", A)

for i in individual:
    fitness -= B[i - 1][0] * B[i - 1][1] * B[i][1]
    B[i - 1][1] = B[i][1]
    B[i][0] = B[i - 1][0]
    print("B after ", i, ":", B, fitness)
return fitness


