def myGreeting1():
    print('Good morning')


def myGreeting2():
    print('Good day')


def myGreeting3():
    print('Good evening')


def myGreeting4():
    print('Good night')


def myGreetingRecipient(greetFunction):
    greetRecipient = input("name?")
    print("Dear, ", greetRecipient)
    greetFunction()


# for myGreeting in myGreetingsList:
#     myGreetingRecipient(myGreeting)

def myGreetingCodeTime(greetFunction):
    greetFunction()


myGreetingsList = [myGreeting1, myGreeting2,
                   myGreeting3, myGreeting4]


# enter_code_time = int(input('0 - morning; 1 - afternoon; 2 - evening; 3 - nigh'))
# myGreetingCodeTime(myGreetingsList[enter_code_time])

def checkTimeOfDay():
    while True:
        timeOfDay = input("Input time of day (M-morning;"
                          "D-afternoon;E- everning;N-night):")
        if timeOfDay == "M":
            return myGreetingsList[0]
        elif timeOfDay == "D":
            return myGreetingsList[1]
        elif timeOfDay == "E":
            return myGreetingsList[2]
        elif timeOfDay == "N":
            return myGreetingsList[3]
        else:
            print("Wrong input!")

#
# for i in range(3):
#     myGreetingRecipient(checkTimeOfDay())

# myNumbers=[2, 2.5, 4.56,23]
# for num in myNumbers:
#     print((lambda x:x+10)(num))

students = [['Bob', 70],
 ['Jane', 80],
 ['Andy', 50]
 ]

sort_l = lambda x:sorted(x)
print(sort_l(students))

sort_b = sorted(students, key=lambda x:x[1])

print(sort_b)



byn_To_Dollar = lambda x: (x*bynToDollar)*(1 - discount)

Dollar_byn_To = lambda x: (x/bynToDollar)*(1 - discount)

# while True:
#     enter_currency = input('1 - if currency - byn:\n2 - if currency - dollar:\n3 - close')
#     if enter_currency == '1':
#         for i in range(2):
#             item_price = float(input('enter price'))
#             print(byn_To_Dollar(item_price))
#     elif enter_currency == '2':
#         for i in range(2):
#             item_price = float(input('enter price'))
#             print(Dollar_byn_To(item_price))
#     elif enter_currency == '3':
#         break

bynToDollar=3.02
discount=0.15
byn_To_Dollar = lambda x: x*bynToDollar
byn_To_Dollar_Discount = lambda x: x*bynToDollar*discount

price = float(input("enter price:"))
print(f'product price:{byn_To_Dollar(price):.2f} $')
print(f'discounted price:{byn_To_Dollar(price) - byn_To_Dollar_Discount(price):.2f} $')
print(f'discount:{byn_To_Dollar_Discount(price):.2f} $')


