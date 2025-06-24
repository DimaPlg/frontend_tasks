import copy
num_now = 1
num_befor = 0
rezerv = 0
lenght = int(input('Введите длинну ряда фиб.: '))
for i in range(lenght):
    print(f'{i + 1} член ряда : {num_befor}')
    rezerv = num_now + num_befor
    num_now = num_befor
    num_befor = rezerv

my_list = [1,3,656,345,23]
print(id(my_list))
my_list = [1,3,656,345,23] + [4]
print(id(my_list))
my_list.append(5)
print(id(my_list))

l1 = [1,23,24,132]
l2 = l1
l1.append('re')
print(l2)
l3 = l1.copy()
l1.append(4)
print(l1)
print(l3)

list_m = [1, 24, 5, 2, 'string']
print(list_m[4][3])
list_m[4] +=  'i'
print(list_m[-1])

test_1 = [1,2,3,[1,2,3]]
test_copy = copy.copy(test_1)
print(test_1, test_copy)
test_copy[3].append(4)
print(test_1, test_copy)
test_1 = [1,2,3,[1,2,3]]

new_list = [i for i in test_1]
print(new_list)

list_in = [1, 24, 5, 2, 'string']
#position = int(input(f'enter insert position from 0 to {len(list_in) - 1}'))
position = 2
insert_str = 'fgd'
#list_in = list_in[:position] + [insert_str] + list_in[position:]
print(list_in)
arg = list_in[position]
list_res = [] 
for i in list_in:
    if i == arg:
        list_res.append(insert_str)
        
    list_res.append(i)
print(list_res)
    
        
        
