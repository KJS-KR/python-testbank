# 13909번, 창문 닫기
import sys
input = sys.stdin.readline

# window = {}
# for i in range(1, N+1):
#     if i not in window:
#         window[i] = 0
    
# for i in range(1, N+1): # i번 사람
#     for j in range(i, N+1): # j번 창문
#         if j % i == 0:
#             if window[j] == 0:
#                 window[j] = 1
#             else:
#                 window[j] = 0

# count = 0
# for i in window:
#     if window[i] == 1:
#         count += 1

# print(list(window.values()).count(1))
print(int(int(input())**0.5))  