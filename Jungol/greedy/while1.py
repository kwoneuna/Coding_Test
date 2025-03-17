# a 가 1이 될때 까지면 while 에 a>1을 해야함 헷갈리지말것,,
# N의 값을 줄일때 2개 이상의 수로 나누는 작업이 1을 배는 작업보다 훨씬 수를 많이 줄일 수 있기 때문
a,b = map(int,input().split())

count = 0
while a > 1:
    if a % b == 0:
        count += 1
        a /= b
    else:
        count += 1
        a -= 1
print(count)

#################################################
#이런식으로 code 작성하면 log(b)로 할 수 있다 
while True:
    # N이 K로 나누어 떨어지는 수가 될 수 있을 때 까지 빼기
    target = (a//b) * b
    count += (a-target) # 1을 빼는 연산을 몇번 수행할지 
    if a<b:
        break
    count += 1
    a //= b
count += (a-1)
print(count)