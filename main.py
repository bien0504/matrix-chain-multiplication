import genetic_algorithm
import random
# define int_max value
int_max = float('inf')
def init_random_data(n,a,b):
    random_numbers = [random.randint(a, b) for _ in range(n)]
    random_numbers_str = ",".join(map(str, random_numbers))
    with open('data.txt', 'w') as file:
        file.write(random_numbers_str)

init_random_data(100,5,10)

#get data from file
with open('data.txt', 'r') as file:
    data = file.read().split(',')

data = [int(num) for num in data]
n = len(data)
print(data)

s = [[0] * n for _ in range(n + 1)]  # index
m = [[0] * n for _ in range(n + 1)]  # cost A[i:j]

A = [{} for _ in range(n)]

for i in range(1, n):
    A[i] = [data[i - 1], data[i]]
    m[i][i] = 0  # chain length 1

def dp():

    for l in range(2, n + 1):  # chain length l
        for i in range(1, n - l + 1):  # chain begins at A[i]
            j = i + l - 1  # chain ends at A[j]
            m[i][j] = int_max
            for k in range(i, j):  # Try Ai:k Ak+1:j
                q = m[i][k] + m[k + 1][j] + A[i][0] * A[k][1] * A[j][1]
                if q < m[i][j]:
                    m[i][j] = q  # remember this cost
                    s[i][j] = k  # remember this index
    print("Cost:", m[1][n - 1])
    print("Order:", result(s, 1, n - 1))
    # with open('result.txt', 'w') as file:
    #     file.write( str(m[1][n - 1]))
    #     file.write( str(result(s, 1, n - 1)))

def greedy():#select the min cost first
    result=0
    cost = [0 for _ in range(n-1)]
    for i in range(n-2):
        cost[i]=A[i+1][0]*A[i+1][1]*A[i+2][1]
    del A[0]
    del cost[-1]
    while len(cost)>1:
        min_cost=min(cost)
        index=cost.index(min_cost)
        result+=min_cost
        A[index][1]=A[index+1][1]
        del A[index+1]
        # cost[index-1]=A[index-1][0]*A[index-1][1]*A[index][1]
        # cost[index+1]=A[index][0]*A[index][1]*A[index+1][1]
        if index==0:
            cost[index + 1] = A[index][0] * A[index][1] * A[index + 1][1]
            del cost[0]
        elif index==len(cost)-1:
            cost[index - 1] = A[index - 1][0] * A[index - 1][1] * A[index][1]
            del cost[index]
        else:
            cost[index - 1] = A[index - 1][0] * A[index - 1][1] * A[index][1]
            cost[index + 1] = A[index][0] * A[index][1] * A[index + 1][1]
            del cost[index]
    assert len(cost)==1
    result+=cost[0]
    print(result)

def result(s, i, j):
    if i == j:
        return str(i)
    else:
        res = []

        res.append("(")

        left_str = result(s, i, s[i][j])
        res.append(left_str)

        right_str = result(s, s[i][j] + 1, j)
        res.append(right_str)
        res.append(")")

        return "".join(res)

# genetic_algorithm(n=n, population_size=100, mutation_rate=0.01, generations=100)


# dp()
# greedy()
genetic_algorithm()
