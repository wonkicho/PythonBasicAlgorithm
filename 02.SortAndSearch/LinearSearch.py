#시간복잡도 O(n), 최악의 경우 모든 원소 다 비교해야됨

def linear_search(L, x):
    i = 0
    while i<len(L) and L[i] !=x:
        i +=1
        
    if i < len(L):
        return i
    else:
        return -1
    
    
if __name__ == "__main__":
    L = [1,4,6,2,3,7]
    result = linear_search(L, 3)
    print(result)