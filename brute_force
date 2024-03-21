from itertools import permutations
import get_data
def generate_permutations(n):
    numbers = list(range(1, n+1))  # Tạo danh sách các số từ 1 đến n
    perm_list = list(permutations(numbers))  # Tạo tất cả các hoán vị của danh sách số
    return perm_list

def solve(data):
    data = [int(num) for num in data]
    data = [[data[i], data[i + 1]] for i in range(0, len(data) - 1)]

if __name__=="__main__":
    n = 10
    permutations_list = generate_permutations(n)
    for perm in permutations_list:
        perm = list(perm)
        print(perm)

