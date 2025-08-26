from random import random

class Student_Id:
    id_student_list = []

    def add_id(swlf, id_student_list, new_id):
        return id_student_list.append(new_id)



class Student:

    unuv = 'BGU'

    def __init__(self, name, last_name, age):
        self.__name = name
        self.last_name = last_name
        self.age = age
        # def check_unic(first_val, last_val):
        #     student_list = Student_Id.id_student_list()
        #     while True:
        #         num = random.randint(first_val, last_val)
        #         if num not in student_list:
        #             student_list.append(num)
        #             return num
        #     return False
        # self.__personal_ID = random.randint(1, 11111)

    def get_info(self):
        return f'{self.__name}, {self.last_name}, {self.age}, {self.unuv}'

    def set_attribute(self, class_name, atr_name, atr_new_val):
        if hasattr(class_name, atr_name):
            setattr(class_name, atr_name, atr_new_val)

    def get_say_hi(self, temp):
        return f'Hi, {temp}'




st1 = Student('Dima', 'Plushkin', 21)
st2 = Student('Sasha', 'Brando', 22)

print(st2.get_info())
print(st1.get_info())
st1.last_name = 'get'

print(st1.get_info())

# st1.set_attribute(st1, 'name', 'Kostiy')
#
# print(st1.get_info())
# print(st1.get_say_hi(f'my name {st1.name}'))
print(Student.__name())
