# 괄호, 9012번
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    par = input()
    while(par.find("()") != -1):
        par = par.replace("()", "")
    # print(par)
    # print(len(par))
    if len(par) <= 1:
        print("YES")
    else:
        print("NO")    