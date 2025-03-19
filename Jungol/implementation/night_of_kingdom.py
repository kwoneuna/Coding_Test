inputs = input()
strings = [chr(i) for i in range(97,123)]
x_index = strings.index(inputs[0]) + 1 
y_index = int(inputs[1])
dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]
cnt = 0
for i in range(len(dx)):
    tmp_x = x_index + dx[i]
    tmp_y = y_index + dy[i]
    if tmp_x < 1 or tmp_x > 8 or tmp_y < 1 or tmp_y > 8:
        continue
    else :
        cnt +=1 
print(cnt)