import get_data
import time
int_max = float('inf')
# start=time.time()
def solve(data):
    """Dynamic Programming approach for Matrix Chain Multiplication."""
    start_time=time.time()
    n = len(data)
    s = [[0] * n for _ in range(n + 1)]  # index
    m = [[0] * n for _ in range(n + 1)]  # cost A[i:j]
    A = [{} for _ in range(n)]

    for i in range(1, n):
        A[i] = [data[i - 1], data[i]]
        m[i][i] = 0  # chain length 1

    for l in range(2, n + 1):  # chain length l
        for i in range(1, n - l + 1):  # chain begins at A[i]
            j = i + l - 1  # chain ends at A[j]
            m[i][j] = int_max
            for k in range(i, j):  # Try Ai:k Ak+1:j
                q = m[i][k] + m[k + 1][j] + A[i][0] * A[k][1] * A[j][1]
                if q < m[i][j]:
                    m[i][j] = q  # remember this cost
                    s[i][j] = k  # remember this index
    dptime=time.time()-start_time
    print("result of dp algorithm:",m[1][n - 1])
    return m[1][n - 1], dptime,result(s, 1, n - 1)

def result(s, i, j):
    """Constructs the optimal parenthesization."""
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
if __name__ == "__main__":
    data=get_data.get_data()
    print(data)
    cost,ptime,order=solve(data)
    print(cost)
    print(ptime)
    print(order)
