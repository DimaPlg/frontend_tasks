num = float(input('Enter float number:'))
revers_num = 0
l_num = len(str(num))

num = float(num)
modif = 1
if num < 0:
    modif = -1
    num*=-1

max_pow = 0
min_pow = 0


while num > 0:
    if num / 10**max_pow < 10:
        break
    max_pow+=1

while num > 0:
    if num * 10**min_pow == int(num):
        break
    min_pow-=1


