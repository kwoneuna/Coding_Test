#https://jungol.co.kr/problem/1692?cursor=NiwxLDA=
# 곱셈 하는 방법을 print하는 방법
import sys
inputs = sys.stdin.read().split()
a,b = map(int,inputs[:2])

m = b // 100
n = (b-m*100) // 10
l = b - m*100 - n*10
# print(m,n,l)
print(f'{l*a}')
print(f'{n*a}')
print(f'{m*a}')
print(f'{a*b}')