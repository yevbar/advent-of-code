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
  input_[1] = 12
  input_[2] = 2
  print(evaluate(input_))