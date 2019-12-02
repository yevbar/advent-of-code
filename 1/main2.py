def get_sum(value):
    if value <= 8:
        return 0
    fuel_needed = (value // 3) - 2
    return fuel_needed + get_sum(fuel_needed)
sum = 0

with open("input.txt") as f:
    line = f.readline()
    while line:
        cur_value = int(line)
        fuel_needed = get_sum(cur_value)
        sum += fuel_needed
        line = f.readline()

print(sum)