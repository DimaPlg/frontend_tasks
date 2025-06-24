def push(num, change_list):
    change_list.append(num)
    return change_list

def pop(change_list):
    change_list.pop()
    return change_list


stack_brackets = '((){}[]())'
stack_brackets_list = list(stack_brackets)
stack_reserved_space = [stack_brackets_list[0]]
stack_brackets_list_len = len(stack_brackets_list)

brackets_dict = {
    ')':'(',
    '}':'{',
    ']':'[',
}
check_line = '(){}[]'

for index in range(1, stack_brackets_list_len):
    if brackets_dict.get(stack_brackets_list[index]) == stack_reserved_space[-1]:
        pop(stack_reserved_space)
    elif stack_brackets_list[index] in check_line:
        push(stack_brackets_list[index], stack_reserved_space)



if len(stack_reserved_space) > 0:
    print(f'line {stack_brackets} asymmetrically')
else:
    print(f'line {stack_brackets} symmetrically')

stack_num = '13641643'
stack_num_list = list(stack_num)
stack_num_reserved_space = [stack_num_list[0]]
stack_num_list_len = len(stack_num_list)
start_index_stak = -1
index = 1

while index < stack_num_list_len:
    if stack_num_list[start_index_stak] == stack_num_reserved_space[-1]:
        pop(stack_num_reserved_space)
        start_index_stak -=1
        if index < -start_index_stak:
            break

    else:
        push(stack_num_list[index], stack_num_reserved_space)
        index+=1

if len(stack_num_reserved_space) > 0:
    print(f'line {stack_num} asymmetrically')
else:
    print(f'line {stack_num} symmetrically')