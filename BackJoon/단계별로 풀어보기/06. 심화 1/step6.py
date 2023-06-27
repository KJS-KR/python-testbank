# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.


C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    
    total = 0
    for j in range(1, N[0]+1):
        total += N[j]
    avg = total/N[0]
    
    avg_count = 0
    for k in range(1, N[0]+1):
        if N[k] > avg:
            avg_count += 1
    
    ratio = (avg_count/N[0])*100
    
    print("{:.3f}%".format(ratio))