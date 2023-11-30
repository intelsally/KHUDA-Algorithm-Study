#저주의 숫자 3
def solution(n):
    answer = 0
    for i in range(1,n + 1):
        answer += 1
    
        if '3' in str(answer ) or (answer) %3 == 0 :
            answer += 1
        
    return answer

#평행
def solution(dots):
    m_list = []
    answer = 0

    m1 = ((dots[0][0] - dots[1][0])/(dots[0][1] - dots[1][1]))
    m2 = ((dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]))

    m3 = ((dots[0][0] - dots[2][0])/(dots[0][1] - dots[2][1]))
    m4 = ((dots[1][0] - dots[3][0])/(dots[1][1] - dots[3][1]))

    m5 = ((dots[0][0] - dots[3][0])/(dots[0][1] - dots[3][1]))
    m6 = ((dots[2][0] - dots[1][0])/(dots[2][1] - dots[1][1]))

    if m1==m2 or m3== m4 or m5 == m6:
        return 1
    else: return 0

#겹치는 선분의 길이
def solution(lines):
    set_list = [set(range(l[0],l[1])) for l in lines]
    return len((set_list[1] & set_list[0])| (set_list[1] & set_list[2]) | (set_list[2] & set_list[0]))

#유한소수 판별하기
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1: return 1
    else: return 2