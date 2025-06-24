# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# stackObject = Stack()
#
# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)
# print(stackObject.pop())
# print(stackObject.pop())
# print(stackObject.pop())

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum


# stackObject1 = Stack()
# stackObject2 = Stack()
# stackObject1.push(3)
# stackObject2.push(stackObject1.pop())
# print(stackObject2.pop())

# littleStack = AddingStack()
# anotherStack = AddingStack()
# funnyStack = AddingStack()
# littleStack.push(1)
# anotherStack.push(littleStack.pop() + 1)
# funnyStack.push(anotherStack.pop() - 2)
# print(funnyStack.pop())

# l = AddingStack()
# l.push(2)
# l.push(3)
# l.push(1)
# print(l.getSum())
# print(l.pop())
# print(l.getSum())
# print(l.__dict__)

# class ExampleClass:
#     def __init__(self, val=1):
#         self.first = val
#
#     def setSecond(self, val):
#         self.second = val


# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject2.setSecond(3)
# exampleObject3 = ExampleClass(4)
# exampleObject3.third = 5
# exampleObject3.setSecond(1)
# print(exampleObject1.__dict__)
# print(exampleObject2.__dict__)
# print(exampleObject3.__dict__)

#
# class ExampleClass:
#     def __init__(self, val=1):
#         self.__first = val
#
#     def setSecond(self, val=2):
#         self.__second = val
#
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject2.setSecond(3)
# exampleObject3 = ExampleClass(4)
# exampleObject3.__third = 5
# print(exampleObject1.__dict__)
# print(exampleObject2.__dict__)
# print(exampleObject3.__dict__)


# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
#
# print(exampleObject1.__dict__, exampleObject1.counter)
# print(exampleObject2.__dict__, exampleObject2.counter)
# print(exampleObject3.__dict__, exampleObject3.counter)

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)
print(ExampleClass.__dict__)
print(exampleObject.__dict__)