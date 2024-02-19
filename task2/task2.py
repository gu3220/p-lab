import linecache

path_circle, path_points = input().split()

center_x, center_y = map(int, linecache.getline(path_circle, 1).strip().split(' '))
radius = int(linecache.getline(path_circle, 2).strip())
answ = []

def check_point(x, y):
    dist = (x - center_x)**2+(y-center_y)**2
    if (dist == radius ** 2):
        return '0'
    elif (dist < radius ** 2):
        return '1'
    else:
        return '2'

with open(path_points) as file:
     for line in file:
         x, y = map(int, line.strip().split(' '))
         check_point(x, y)
         answ.append(check_point(x, y))

print('\n'.join(answ))