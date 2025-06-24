#print('second arg: {one}, first arg: {}'.format(2, one = 1))
#print('Hi {age:d}, you age is: {name}'.format(name = 'Alice', age = 18))
#print('Int:{:20d}cool'.format(8))
#print('{:2s}'.format('Masha'))
#print('{:^7.1f}'.format(3.14))
#print('{:^7d}'.format(3))
#print('{:=^9d}'.format(326))
#print('{:0<9d}'.format(3))
#print('{:10} - Питончик'.format('Python'))
#print('{:>10}'.format('Py'))
#print('{:^10}'.format('Py'))
#print('{:_^10}'.format('Py'))
#print('{:.2}'.format('Python'))
#print('{:10.2} питончик'.format('Python'))
#print('{:_^6.2} питончик'.format('Python'))

strin = '{:{заполнитель}{выравнивание}{ширина}}'
print(strin.format('Питон', заполнитель = '_', выравнивание = '^', ширина = 9))

strin = '{:{}{}{}}'
print(strin.format('Питон', '_', '^', 9))



