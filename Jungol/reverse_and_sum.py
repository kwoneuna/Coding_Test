#https://jungol.co.kr/problem/1009?cursor=NiwzLDA=
#string & 조건부
import sys
datas = [list(map(int,line.split())) for line in sys.stdin.read().strip().split("\n")]

for i in datas:
    num = i[0]
    if num == 0:
        exit()
    else:
        dig = [int(number) for number in str(num)]
        m = 0
        for i in dig:
            m+=i
        reverse_num = ''.join(map(str,str(num)[::-1]))
        no_start= True
        for i in reverse_num:
            if no_start and  i =='0':
                continue
            else:
                no_start = False
                print(i,end='')
        print(end=' ')
        print(m)

