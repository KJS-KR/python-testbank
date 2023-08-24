# 27433번, 팩토리얼 2

n = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
print(factorial(n))