# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

S = input()

c_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s_count = 0

for s in c_list:
    s_count += S.count(s)
    if s in S:
        S = S.replace(s, '*')
    

print(len(S))
        
        
    