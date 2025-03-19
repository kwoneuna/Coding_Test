a = list(input())

result = 0
for i in a:
    if  result == 0 or i == '0' or i == '1':
        result += int(i)
    else:
        i = int(i)
        result *= i
print(result)

###########
# data = input()
# result = int(data[0])
# for i in range(1,len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)