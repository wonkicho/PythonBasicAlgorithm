"""
인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2
"""

#재귀
def solution_recurr(x):
    if x<=1:
        return x
    else:
        return solution(x-2) + solution(x-1)
    
#반복
def solution_iter(n):
    if n<=1:
        return n
    
    a, b= 0, 1
    for i in range(n-1):
        a,b = b, a+b
    return b

solution(5)