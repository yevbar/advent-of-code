sum = 0

with open("input.txt") as f:
    line = f.readline()
    while line:
        cur_value = int(line)
        fuel_needed = (cur_value // 3) - 2
        sum += fuel_needed
        line = f.readline()

print(sum)