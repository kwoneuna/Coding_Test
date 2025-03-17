a = input()
b = map(int,input().split())

b = sorted(b)
result = 0
count = 0

for i in b:
    count += 1
    if count >= i:
        result += 1
        count =0
print(result)