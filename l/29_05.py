# def sendMsg():
#     msg = ''
#     def createMsg(info):
#         nonlocal msg
#         msg +=info
#         return msg
#     return createMsg
#
#
#
# s =sendMsg()
# s('Dima')
# print(s(' Hi!'))
#
# def sendMsg(userTo):
#     def setUserFromMsg(userFrom):
#         def setLanguage(language):
#             def setMsgTxt(msgTxt):
#                 print("Dear {}, Hello from {}. Welcome to {} world! {}".
#                       format(userTo, userFrom, language, msgTxt))
#
#             return setMsgTxt
#
#         return setLanguage
#
#     return setUserFromMsg
#
#
# sendMsg('Dima')('Shiza')('Durka')('Good luck!')
#
# print(sum([1, 2, 3]))
#
# list1 = [1, 2, 23]
# list2 = [4, 234, 213]
# print(list(zip(list1, list2)))
#
#
# def curry(func):
#     return lambda x1=5: lambda x2: lambda x3=7: lambda c: x1 ** 2 + x2 ** .5 + x3 / (x1 + x2) + c
#
#
# def curry(func):
#     return lambda x2: lambda c: 25 + x2 ** .5 + 7 / (5 + x2) + c
#
#
# from functools import partial
# import math
#
#
# def func(x1, x2, x3, c):
#     return x1 ** 2 + math.sqrt(x2) + x3 / (x1 + x2) + c
#
#
# func_x1_x3_fixed = partial(func, x1=5, x3=7)
#
# assert (func_x1_x3_fixed(x2=16, c=1) == func(5, 16, 7, 1))


# def simpleDecorator(myFunction):
#     print("Hello! I'm Decorator!")
#
#     def simpleWrapper():
#         print("Function starts working...")
#         myFunction()
#         print("See you!")
#
#     return simpleWrapper
#
# def simpleDecorator_v2(myFunction):
#     print("Hello! I'm Second Decorator!")
#     def simpleWrapper():
#         print("Let's start...")
#         myFunction()
#         print("Good luck!")
#     return simpleWrapper
#
# # def sayHi():
# #     print("Welcome!")
#
#
# # def sayHi():
# #     print("Welcome!")
# #
# #
# # def sayBuy():
# #     print('Buy!')
#
# # sayHi()
# #
# # sayBye = simpleDecorator(sayBuy)
# # sayBye()
#
#
# # simpleDecorator(sayHi)()
#
# @simpleDecorator
# @simpleDecorator_v2
# def sayHi():
#     print("Welcome!")
# sayHi()

def outer(x, y =2):
    print()
    def inner(z=y):
        nonlocal y
        z = y
        return x, z
    x, y = None, None
    return inner

print(outer(10)())