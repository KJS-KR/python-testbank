# 25501번, 재귀의 귀재

n = int(input())

count = 1
def recursion(s, l, r, count):
    if l >= r: return print(1, count)
    elif s[l] != s[r]: return print(0, count)
    else: 
        count += 1
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

for i in range(n):
    word = input()
    isPalindrome(word)