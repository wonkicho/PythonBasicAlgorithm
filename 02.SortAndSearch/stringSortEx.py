

L = ['abcd', 'xyz', 'spam']
#길이순 우선 정렬되게 람다 사용
L2 = sorted(L, key=lambda x : len(x))

#원래는 알파벳 순으로
L3 = sorted(L)
print(L2, L3)