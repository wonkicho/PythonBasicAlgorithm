import time
#리스트의 길이가 길면 시간은 오래 걸린다. 리스트의 길이에 비례하게 됨 O(n)
L = ['Bob', 'Cat', 'Pram']

#리스트에 원소 삽입하기
L.append('New')
print(L)

#리스트에 원소 넣고 삭제하기
start = time.time()
L = [20, 37, 58, 72, 91]
L.insert(3, 65) #3번째 인덱스에 65를 삽입하기
end = time.time()
total_time = end - start
print(L, total_time)

start = time.time()
del(L[2])
end = time.time()
total_time = end - start
print(L, total_time)