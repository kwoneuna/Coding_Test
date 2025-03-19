a = input()
alpha_list = [chr(i) for i in range(65,91)]
string_list = []
number_count = 0
for i in range(len(a)):
    if a[i] in alpha_list:
        string_list.append(a[i])
    else:
        number_count += int(a[i])

string_list = sorted(string_list)
string_list = ''.join(string_list)
if number_count != 0:
    string_list += str(number_count)
print(string_list)

########
#이런식의 함수도 쓸 수 있다 
string_list.sort()
print(''.join(string_list))