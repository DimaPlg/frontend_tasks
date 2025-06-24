'''
count = 0
num = 0
while count < 5:
    if count % 2 == 1:
        count +=1
        num +=1
        continue
    if count == 4:
        print(count)
        break
    print(count)
    print(num)
    count +=1
    num +=1
print('\n')

count = 0
num = 0
while count < 5:
    count +=1
    num +=1
    print(num + count)

number = 1
flag = True
while flag:
    print(number)
    number += 1
    if number == 3:
        flag = False
else:
    print("I’ve counted from 1 to 5!")
'''
#str = 'banana'
#print(str.count('ana'))
check_str = 'banajnana'
substring = 'ana'
index = 0
result = 0
for letter in check_str:
    if letter == substring[index]:
        index +=1
        if index == 3:
            result +=1
            index = 1
    else:
        index = 0
print(result)
    
