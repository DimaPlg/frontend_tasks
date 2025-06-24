# from functools import reduce
#
# a = [1, '2', 3, 4, '5']
# res = reduce(lambda x, y: x + y, a)
#
# print(res)

# first_name = input('Enter your first name:')
# last_name = input('Enter your Last name:')
# # (x + ' ' + y).title()
# upper_registr = lambda x,y: f'{x.title()} {y.title()}'
#
# print(f'{upper_registr(first_name,last_name)}')
#
# user_name = lambda first_name,last_name: "Full user's name: {} {}".format(first_name.title(),last_name.title())
# first_user_name=input("Input your first name:")
# last_user_name=input("Input your last name:")
# print(user_name(first_user_name, last_user_name))

from datetime import datetime

stud_birth_year = [2000, 1997, 2002, 1999, 2007]

stud_age = list(map(lambda birth_year : datetime.now().year - birth_year, stud_birth_year))

print(stud_age)

print(dir(__builtins__))
