def tree_layer(length, descendants):
    layer = 0
    while length > descendants:
        length /= descendants
        layer +=1
        if length == descendants:
            return int(layer)
    return int(layer) - 1

def higher_value(sort_list, first_value_index, second_value_index):
    if sort_list[first_value_index] > sort_list[second_value_index]:
        return first_value_index
    return second_value_index

def change_position(sort_list, changeable_index, replacement_index):
    reserved_value = sort_list[changeable_index]
    sort_list[changeable_index] = sort_list[replacement_index]
    sort_list[replacement_index] = reserved_value

def parent_child_comparison(sort_list, parent_index, last_parent_index, child_index, list_length):
    while parent_index < last_parent_index and child_index < list_length:
        if child_index + 1 < list_length:
            max_value_index = higher_value(sort_list, child_index, child_index + 1)
        else:
            max_value_index = child_index
        max_value_index = higher_value(sort_list, max_value_index, parent_index)
        if max_value_index != parent_index:
            change_position(sort_list, parent_index, max_value_index)
        parent_index +=1
        child_index +=2
    return sort_list

def max_value_by_tree(sort_list, length, layers, descendants):
    while layers > -1:
        start_position = descendants ** layers - 1
        last_value_index = descendants ** (layers + 1) - 1
        start_leaf_position_index = last_value_index
        parent_child_comparison(sort_list, start_position, last_value_index, start_leaf_position_index, length)
        layers -= 1

def sort_by_tree(sort_list, length, layers, descendants):
    while layers > -1:
        max_value_by_tree(sort_list, length, layers, descendants)
        change_position(sort_list, 0, length - 1)
        length -= 1
        layers = tree_layer(length, descendants)
    if higher_value(sort_list, 0, 1) != 1:
        change_position(sort_list, 0, 1)
    return sort_list

num_list2 = [-2124,-1195,-1273,-664,-7424,-4558,-7894,4274,22,-1495,135,3614,2775,1313,59,1670,-4156,4103,-2024,-7783
 -2274,-7577,855,-7338,-7009,-4475,2116,-4160,3983,-1825,4231,-7598,-6487,
1958,2120,-2538,-2647,4051,-760,-337,-3935,3536,-2417,3189,3414,-4000,2700,781,-2079,3285,-4323,
-435,1724,824,-3389,1075,-253,-7626,-6217,2075,2299,-4772,-1061,-2952,-2177,3909,-4527,2761,2963,
-4132,-2773,-7233,1393,-5514,-4659,4264,-6012,2074,-2062,-2869,-386,3200,-6286,2336,1522,-2715,
-5364,-5985,-80,-4980,352,-5490,-426,3389,-2496,2747,-2240, - 111111, 5555]



descendants_tree = 2
length_list = len(num_list2)
depth_tree = tree_layer(length_list, descendants_tree)
print(sort_by_tree(num_list2, length_list, depth_tree, descendants_tree))








