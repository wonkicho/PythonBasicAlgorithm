# 정렬된 상태서 탐색함
# 중간 인덱스 값에서 기준으로 반쪽씩 나눠서 찾는 방법
# 한번 비교가 일어날 때마다 리스트가 반씩 줄여짐
# O(log n)

def solution(L, x):
    
    lower = 0
    upper = len(L) -1
    while lower <= upper:
        mid = (lower + upper) // 2
        mid_value = L[mid]
        if x > mid_value:
            lower = mid + 1
        elif x < mid_value:
            upper = mid -1
        else:
            answer = mid_value
            return mid
            
            

    return -1