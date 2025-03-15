## https://jungol.co.kr/problem/1291?cursor=Niww
## 원하는 범위의 구구단 범위 입력받아 구구단 출력하기
import sys

datas = sys.stdin.read().strip().split("\n")
datas = [list(map(int,line.split())) for line in datas]
def prit(a,b):
    array = [i for i in range(a,b-1,-1)] if a>b else [i for i in range(a,b+1)]
    for i in range(1,10):
        for j in array:
            k = i*j
            print(f"{j} * {i} = {k:2d}", end="   ")

        print("\n")
for data in datas:
    a = data[0]
    b = data[1]
    if a < 2 or a > 9 or b > 9 or b < 2:
        print("INPUT ERROR!")
        continue
    else:
        prit(a,b)
