# 24060번, 알고리즘 수업 - 병합 정렬

# li[p..q]와 li[q+1..r]을 병합하여 li[p..r]을 오름차순 정렬된 상태로 만든다.
# li[p..q]와 li[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(li, p, q, r):
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (li[i] ≤ li[j])
        then tmp[t++] <- li[i++]; # tmp[t] <- li[i]; t++; i++;
        else tmp[t++] <- Ali[j++]; # tmp[t] <- li[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- li[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- li[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 li[p..r]에 저장
        li[i++] <- tmp[t++]; 


def merge_sort(li): # li[p..r]을 오름차순 정렬한다.
    if (p < r): 
        q = (p + r) / 2;       # q는 p, r의 중간 지점
        merge_sort(li, p, q);      # 전반부 정렬
        merge_sort(li, q + 1, r);  # 후반부 정렬
        merge(li, p, q, r);        # 병합