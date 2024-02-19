import sys

n, m = int(sys.argv[1]), int(sys.argv[2])

nums = list(range(1, n+1))
path = []
i = 0
check = 0

while (check != nums[0]):
    for j in range(m):
        if ( j == 0 ):
            path.append(nums[i % len(nums)])
        i += 1
    i -= 1
    check = nums[i % len(nums)]

print(''.join(map(str, path)))
