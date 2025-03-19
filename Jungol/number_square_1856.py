## https://jungol.co.kr/problem/1856?cursor=NiwwLDM=
## 사각형 높이 n, 너비 m 을 입력받아 출력하기
## 문제풀이 1

a,b = map(int,input().split())
k = 1
for i in range(0,a):
    if i % 2 == 0:
        for j in range(k,k + b):
            print(f'{j}',end=' ')
    else:
        for j in range(k+b-1,k-1,-1):
            print(f'{j}',end=' ')
    print()
    k+= b

## 문제풀이2 
# 규칙찾아서 풀어보기
a,b = map(int,input().split())
m = 1

for i in range(0,a):
    if i % 2==0:
        for j in range(m,m+b):
            print(f'{j}',end =' ')
    else:
        tmp = (i+1) * b
        for j in range(tmp, m-1, -1):
            print(f"{j}",end=' ')
    m += b
    print()