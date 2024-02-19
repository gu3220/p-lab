path_array = input()
nums = []

with open(path_array) as file:
    for line in file:
        nums.append(int(line.strip()))

average = round(sum(nums)/len(nums))
moves = sum(list(map(lambda x: abs(average-x), nums)))

print(moves)