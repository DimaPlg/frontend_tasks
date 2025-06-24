a = None
b = 1101
str_var = "string"
print(100/(2*13)//2)
print(hash(a))
print(hash(None))
print(hash(True))
print(hash(str_var))

my_list = [['a','v'], ["f",'d'], "r"]
print(id(my_list))
print(hash(my_list[2]))
my_list.append("mari")
print(id(my_list))

my_t = (3,54,45)
print(my_t)
print(hash(my_t))
print(id(my_t))
my_t += (4,)
print(hash(my_t))
print(id(my_t))
str_t = "sSlDjfDlsAS"

list_t = [i for i in str_t if i.islower() != True]
list_r = list(str_t.split([i for i in str_t if i.isupper() == True]))
print(list_t)

