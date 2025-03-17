a = int(input())
b = input().split()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
x,y = 1,1
def move(x,y,i):
    if i == 'R':
        y = y + 1
    elif i == 'L':
        y = y - 1 
    elif i == 'U':
        x = x - 1 
    elif i == 'D':
        x = x + 1
    return x, y
for i in b:
    tmp_x,tmp_y = move(x,y,i)
    if tmp_x < 1 or tmp_y < 1 or tmp_y > a or tmp_x > a:
        continue
    else:
        x = tmp_x
        y = tmp_y
print(x, y)

#####################
n = int(input())
x, y = 1,1 
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types:
            nx = x + dx[i]
            ny = x + dy[i]
    if nx < 1 or nx < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(nx,ny)