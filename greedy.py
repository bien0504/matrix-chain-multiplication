import get_data
import time
int_max = float('inf')

def solve(data):
    start_time=time.time()
    order = []
    data = [int(num) for num in data]
    data = [[data[i], data[i + 1]] for i in range(0, len(data) - 1)]
    result=0
    B = data
    n=len(B)
    contracted = [[0] * n for _ in range(n)]
    cost=[int_max for _ in range(n)]
    for i in range(1,n):
        cost[i]=B[i-1][0]*B[i][0]*B[i][1]
    for step in range(n-1): #number of contraction
        min_cost=min(cost)
        result+=min_cost
        index = cost.index(min_cost)
        order.append(index)
        contracted[index-1][index]=1
        B[index-1][1]=B[index][1]
        B[index][0]=B[index-1][0]

        cost[index] = int_max

        index1=index
        while (index1 > 0 and contracted[index1 - 1][index1] == 1):
            index1 = index1 - 1
            B[index1] = B[index1 + 1]
        index2=index
        while (index2 < len(B) - 1 and contracted[index2][index2 + 1] == 1):
            index2 = index2 + 1
            B[index2] = B[index2 - 1]
        if(index1>0):
            cost[index1]=B[index1-1][0]*B[index1-1][1]*B[index1][1]
        if(index2<n-1):
            cost[index2+1]=B[index2][0]*B[index2][1]*B[index2+1][1]
    ptime=time.time()-start_time
    print("result of greedy algorithm:",result)
    # print(order)
    return result,ptime,order
if __name__=="__main__":
    data = get_data.get_data()
    solve(data)
