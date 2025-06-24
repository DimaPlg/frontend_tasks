def checking_num_tree(length):
    result = length**(1/2)
    if result == int(result):
        return int(result)
    return int(length**(1/2) + 1)

def checking_line_tree(length):
    line_tree = 0
    while length > 2 or length == 2:
        length /= 2
        line_tree += 1
    return line_tree

def max_value(sort_list, first_value_index, second_value_index, third_value_index, forth_value):
    if (sort_list[first_value_index] < sort_list[second_value_index] and sort_list[third_value_index] < sort_list[second_value_index]
            and sort_list[forth_value] < sort_list[second_value_index]):
        return second_value_index
    elif (sort_list[second_value_index] < sort_list[third_value_index] and sort_list[first_value_index] < sort_list[third_value_index]
          and sort_list[forth_value] < sort_list[third_value_index]):
        return third_value_index
    elif (sort_list[second_value_index] < sort_list[forth_value] and sort_list[first_value_index] < sort_list[forth_value]
          and sort_list[third_value_index] < sort_list[forth_value]):
        return forth_value
    return first_value_index

def sort_tree(sort_list, begin_index, last_index):
    level_tree = checking_line_tree(last_index - begin_index) - 1
    length = 2**level_tree + begin_index
    res = last_index - 1
    while True:
        iteration = int(begin_index + 2 ** level_tree - 1)
        while iteration < length:
            check_index_v = 2 ** (level_tree + 1) + begin_index
            if check_index_v > last_index - 1:
                if sort_list[iteration] < sort_list[check_index_v - 1]:
                    res = check_index_v -1
                else:
                    res = iteration
            else:
                res = max_value(sort_list, res, iteration, check_index_v, check_index_v - 1)
            iteration += 1
        level_tree -= 1
        length = 2 ** level_tree + begin_index

        if level_tree < 0:
            return res

def biggest_value(sort_list, index_list):
    #list_value = [sort_list[i] for i in index_list]
    list_value = []
    for i in index_list:
        list_value.append(sort_list[i])
    return sort_tree(list_value, 0, len(list_value))

def sorter(sort_list):
    length = len(sort_list)
    num_trees = checking_num_tree(length)
    length_index_list = num_trees
    list_max_value_trees = [0]*num_trees
    for tree in range(num_trees):
        begin_index = tree * num_trees
        last_index = (tree + 1) * num_trees
        if last_index > length:
            last_index = length
        list_max_value_trees[tree] = sort_tree(sort_list, begin_index, last_index)
    while True:
        change_v_index = biggest_value(sort_list, list_max_value_trees)
        max_value_index = list_max_value_trees[change_v_index]
        reserved = sort_list[length - 1]
        sort_list[length - 1] = sort_list[max_value_index]
        sort_list[max_value_index] = reserved

        length -= 1
        if length - 1 < (num_trees - 1) * length_index_list:
            num_trees -= 1
            if num_trees == 0:
                print(sort_list)
                return sort_list
        begin_index = change_v_index * length_index_list
        last_index = (change_v_index + 1) * length_index_list
        if last_index > length - 1:
            last_index = length
        list_max_value_trees[change_v_index] = sort_tree(sort_list,begin_index, last_index)
        begin_index = (num_trees - 1) * length_index_list
        last_index = length
        list_max_value_trees[- 1] = sort_tree(sort_list,begin_index, last_index)

num_list2 = [-2124,-1195,-1273,-664,-7424,-4558,-7894,4274,22,-1495,135,3614,2775,1313,59,1670]
# ,272,-3907,-6679,
#             -4156,4103,-2024,-7783,-2274,-7577,855,-7338,-7009,-4475,2116,-4160,3983,-1825,4231,-7598,-6487,
#             1958,2120,-2538,-2647,4051,-760,-337,-3935,3536,-2417,3189,3414,-4000,2700,781,-2079,3285,-4323,
#             -435,1724,824,-3389,1075,-253,-7626,-6217,2075,2299,-4772,-1061,-2952,-2177,3909,-4527,2761,2963,
#             -4132,-2773,-7233,1393,-5514,-4659,4264,-6012,2074,-2062,-2869,-386,3200,-6286,2336,1522,-2715,
#             -5364,-5985,-80,-4980,352,-5490,-426,3389,-2496,2747,-2240
sorter(num_list2)
