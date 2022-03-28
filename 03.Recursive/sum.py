#재귀 호출의 종결 조건 필요!

def sum(n):
    if n <= 1:   
        return n
    else:
        return n + sum(n-1)

a = int(input("Number: "))
print((sum(a)))