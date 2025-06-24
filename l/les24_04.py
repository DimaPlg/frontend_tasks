import random


def info_customer(customer_name, list_customers):
    template = f'{customer_name} on position :'
    customer_repeat_counter = 0
    for customer_position_index in range(len(list_customers)):
        if list_customers[customer_position_index] == customer_name:
            template += f'\n{customer_position_index} '
            customer_repeat_counter += 1
    if customer_repeat_counter > 1:
        template += f'\n{customer_name} have a discount!'
        print(template)


def generate_customer_dict(customer_list):
    customer_dict = {}
    for customer_position_index in range(len(customer_list)):
        if customer_list[customer_position_index] not in customer_dict:
            customer_dict[customer_list[customer_position_index]] = [[1], customer_position_index]
        else:
            customer_dict[customer_list[customer_position_index]][0][0] += 1
            customer_dict[customer_list[customer_position_index]] += [customer_position_index]

    return customer_dict


def output_customer_with_discount(customer_dict):
    for customer in customer_dict:
        if customer_dict[customer][0][0] > 1:
            print(f'{customer} on position {customer_dict[customer][1:]} have discount!')


def count_average_num_list(list_num):
    sum_num_list = 0
    length = 0
    for num in list_num:
        sum_num_list += num
        length += 1
    return sum_num_list / length


def arithmetic_mean(*args):
    numbers_sum, count_nums = 0
    for num in args:
        numbers_sum += num
        count_nums += 1
    return numbers_sum / count_nums


def list_gen(length_list, min_value_list, max_value_list):
    return [random.randint(min_value_list, max_value_list) for num in range(length_list)]


customerList = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick', 'Anna']
set_customer = set(customerList)
#
# for customer in set_customer:
#     info_customer(customer, customerList)


output_customer_with_discount(generate_customer_dict(customerList))
l = list_gen(100, -46, 232)
print(l)
print(count_average_num_list(l))


def output_login_password_user(user_list):
    for login, password in user_list:
        print(f'User login: {login}\nuser password: {password}')


users = [['user1', '111'], ['user2', '2222'], ['user3', '33333']]

output_login_password_user(users)
