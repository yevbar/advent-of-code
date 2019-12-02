def evaluate(input_):
  cur_index = 0
  while input_[cur_index] != 99:
    opcode = input_[cur_index]
    index_1 = input_[cur_index+1]
    index_2 = input_[cur_index+2]
    index_3 = input_[cur_index+3]
    if opcode == 1:
      input_[index_3] = input_[index_1] + input_[index_2]
      cur_index += 4
    if opcode == 2:
      input_[index_3] = input_[index_1] * input_[index_2]
      cur_index += 4
  return input_[0]

with open('input.txt') as f:
  input_ = f.read().split(',')
  input_ = [int(x) for x in input_]
  for i in range(100):
    for j in range(100):
      input_clone = input_.copy()
      input_clone[1] = i
      input_clone[2] = j
      if evaluate(input_clone) == 19690720:
        print("WE FOUND IT")
        print(100 * i + j)