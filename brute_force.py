from itertools import permutations
import get_data
import copy
import time
int_max = float('inf')
def generate_permutations(n):
    numbers = list(range(1, n+1))  # Tạo danh sách các số từ 1 đến n
    perm_list = list(permutations(numbers))  # Tạo tất cả các hoán vị của danh sách số
    return perm_list

def solve(data):
    start_time=time.time()
    record=int_max
    data = [int(num) for num in data]
    data = [[data[i], data[i + 1]] for i in range(0, len(data) - 1)]
    n=len(data)
    perm_list=generate_permutations(n-1)
    order=[[]*n for _ in range(n-1)]
    for perm in perm_list:
        B = copy.deepcopy(data)
        result=0
        contracted = [[0] * n for _ in range(n)]
        for i in perm:
            result+= B[i - 1][0] * B[i][0] * B[i][1]
            B[i - 1][1] = B[i][1]
            B[i][0] = B[i - 1][0]
            contracted[i - 1][i]=1
            index1 = i
            while (index1 > 0 and contracted[index1 - 1][index1] == 1):
                index1 = index1 - 1
                B[index1] = B[index1 + 1]
            index2 = i
            while (index2 < len(B) - 1 and contracted[index2][index2 + 1] == 1):
                index2 = index2 + 1
                B[index2] = B[index2 - 1]
        if(result<record):
            record=result
            order=perm
            # print("new record:",record)
    print("result of bruteforce programming:",record)
    ptime=time.time()-start_time
    return record,ptime,order

if __name__=="__main__":
    data=get_data.get_data()
    solve(data)