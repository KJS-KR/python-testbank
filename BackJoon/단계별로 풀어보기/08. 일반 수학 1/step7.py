# 2869번, 달팽이는 올라가고 싶다.

A, B, V = map(int, input().split())

k = (V - B) / (A - B)

print(int(k) if k == int(k) else int(k) + 1)