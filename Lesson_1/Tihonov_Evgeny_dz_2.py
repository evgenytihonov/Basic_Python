cubes_list = []
new_cubes_list = []
sum_numbs = 0

for i in range(1, 1000, 2):
    cubes_list.append(i ** 3)

for ind, val in enumerate(cubes_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_numbs += cubes_list[ind]

print(sum_numbs)

for m in cubes_list:
    new_cubes_list.append(m + 17)
