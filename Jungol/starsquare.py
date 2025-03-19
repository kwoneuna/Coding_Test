#https://jungol.co.kr/problem/1523?cursor=NiwyLDA=
#center 배우기 !
a,b = map(int,input().split())

def print_star(a,b):
    if b ==1:
        for i in range(1,a+1):
            print("*"*i)
    elif b == 2:
        for i in range(a,0,-1):
            print('*'*i)
    else:
        for i in range(a):
            n = 2*i + 1
            star= '*'*n
            star = star.center(2*a-1,' ')
            print(star)

if b < 1 or b > 3 or a >100 or a<1:
    print('INPUT ERROR!')
else:
    print_star(a,b)
