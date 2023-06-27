# 14215번, 세 막대

# 삼각형 조건, 가장 큰 선이 작은 두 선의 합보다 작아야한다.

# 1. 가장 큰 값을 찾는다
# 2. 작은 두 값의 합을 구한다
# 3. 가장 큰 값이 작은 두 값의 합보다 클 경우 큰 선의 길이는 두 값의 합보다 1 작은 수이다.
# 4. 가장 큰 값이 작은 두 값의 합보다 작을 경우 큰 선의 길이는 가장 큰 값이 된다.

# a, b, c = map(int, input().split())

# list_t = [a, b, c]
# counter = {}

# for i in list_t:
#         if i in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1

# if 3 in counter.values():
#     result = max(list_t)*3
# elif 2 in counter.values():
#     result = min(list_t)*3
# else:
#     if max(list_t) >= sum(list_t) - max(list_t):
#         result = (sum(list_t) - max(list_t)) * 2 -1
#     else:
#         result = sum(list_t)

# print(result)

li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(res)