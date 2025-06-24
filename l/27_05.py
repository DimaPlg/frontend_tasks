# def sayUserHello(user):
#     msg = "Hello, " + user
#     def showMsf():
#         print(msg + "! Let's start...")
#     showMsf()
#
# sayUserHello('user')

# def sayUserHello(user):
#     msg = "Hello, " + user
#     def showMsf():
#         nonlocal msg
#         msg = "Student"
#         print(msg + "! Let's start...")
#     showMsf()
#     print(msg)
#
# sayUserHello('user')
#
#
# def sayUserHello(user):
#     msg ="Hello, " + user
#     def showMsf():
#         print(msg + "! Let's start...")
#     return showMsf
#
# sayUserHello('georg')()
#
#
# def doExercise1(var1):
#     # var2 = 5
#     def doExercise2(var3):
#         return var1**var3
#     return doExercise2
#
# case1=doExercise1(2)
# print(case1(5)) #32
# print(case1(10)) #1024
#


def sayHi(user):
    msg = 'Hi ' + user
    count = 0
    def counter():
        nonlocal count
        count+=1
        return f'{msg} {count}'
    return counter()

i = sayHi('y')
for i in range(5):
    print(i())

def launchСounter():
    counter = 0
    def incrementCounter():
        nonlocal counter
        counter += 1
        return counter
    return incrementCounter

n = launchСounter()
for i in range(5):
    print(n())
