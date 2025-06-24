# def simpledecorartor(x, fun):
#     def increase(y=x):
#         return fun(y) + y
#     return increase
#
# def num(a):
#     return a**2

# print(simpledecorartor(3, num)())
#
# def simpleDecorator_v3(myFunction):
#     print("Hello! I'm Third Decorator!")
#     def simpleWrapper():
#         print("Function starts working...")
#         resutl=myFunction()
#         print("See you!")
#         return resutl
#     return simpleWrapper
# def calculateSum():
#     print("Welcome! Let's calculate...")
#     x=int(input("x: "))
#     y=int(input("y: "))
#     return x+y
#
# # calculateSum = simpleDecorator_v3(calculateSum)
# # print(calculateSum())
#
# def simpleDecorator_v4(myFunction):
#     print("Hello! I'm Fourth Decorator!")
#     def simpleWrapper(argX, argY):
#         print("I've got {},{}. Function starts working...".format(argX, argY))
#         resutl=myFunction(argX, argY)
#         print("See you!")
#         return resutl
#     return simpleWrapper
#
# def calculateSum_v1(a,b):
#     print("Welcome! Let's calculate...")
#     x=int(input("x: "))
#     y=int(input("y: "))
#     return x+y+a+b
#
# calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)
# print(calculateSum_v1(3,4))

# def decoratorWrapper(argForDec):
#     print("I've got arg={} for decorator!".
#     format(argForDec))
#     def simpleDecorator_v5(myFunction):
#         print("Hello! I'm Decorator with arg={}!".
#         format(argForDec))
#         def simpleWrapper(argX, argY):
#             print("Hi! I am Funcion. I've got {},{}. Function starts working...".format(argX, argY))
#             result=myFunction(argX, argY)+argForDec
#             print("See you!")
#             return result
#         return simpleWrapper
#     return simpleDecorator_v5
#
# decoratorWithArg =decoratorWrapper(10)
#
# def calculateSum_v1(a,b):
#     print("Welcome! Let's calculate...")
#     x=int(input("x: "))
#     y=int(input("y: "))
#     return x+y+a+b
#
# calculateSum_v1 = decoratorWithArg(calculateSum_v1)
# print(calculateSum_v1(3,4))

def priceDiscountDecoratorWrapper(discount):
    print('Discount decorator')

    def priceDiscountAddFunDecoratorWrapper(fun):
        print('Add discount')
        print("Hello! I'm Decorator with arg={}!".format(discount))

        def simpleWrapper(price_list, corse):
            print('I\'ve got list of prices with discount: {},'
                  'price list: {}, course: {}.Function starts working...'.format(discount, price_list, corse))
            print('Result working of decorator: ')
            return [price * (1 - discount / 100) for price in fun(price_list, corse)]

        return simpleWrapper

    return priceDiscountAddFunDecoratorWrapper


decoratorWithArg = priceDiscountDecoratorWrapper(15)


def convertToRub(price_list, corse):
    print('Convert from usd to rub')
    return list(map(lambda x, y=corse: x * y, price_list))


# [price * corse for price in price_list]

pricesUSD = [100.34, 35, 67.99, 25.5]
course = 2.9

# print(decoratorWithArg(convertToRub)(pricesUSD, discount))
print(convertToRub(pricesUSD, course))
# print(convertToRub(pricesUSD, 2.6))
#
# c = priceDiscountDecoratorWrapper(convertToRub)
# print(c(16))

# price = 100
# discount = 15
#
# i = price * (1 - discount / 100)
#
# n = price * (discount / 100)
#
# print(f'{i} {price - n}')

# l = [p if print(p) for p in pricesUSD]
# print(l)
