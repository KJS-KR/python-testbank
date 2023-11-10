# 9663번, N-Queen

n = int(input())
row = [0] * n
ans = 0


def promissing(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def n_queen(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if promissing(x):
                n_queen(x+1)


n_queen(0)
print(ans)
