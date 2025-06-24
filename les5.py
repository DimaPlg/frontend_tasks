def took_ambr(val):
    if val == 2 and val == 3:
        if val == 2:
            print("Тут как по кайфу, хош бери хош не бери...")
        else:
            print("Тут без вариков, ток под зонт или больничный..")
    else:
        print("Зонт не бери, черт!")
            
       
        
        

def chek_input():
    str_temp = "Предскажите погоду: \n 1 - ясно \n 2 - пасмурно \n 3 - дождь \n"
    val = int(input(str_temp))
    if 0 < val and val < 4:
        took_ambr(val)
    else:
        print("Хех, промазал")
    

str1 = "())({}}{()][]["
mas_bras = {"[":0,"]":0,"{":0,"}":0,"(":0,")":0}
for i in str1:
    mas_bras[i] += 1
print(mas_bras["["] - mas_bras["]"])
print(mas_bras["{"] - mas_bras["}"])
print(mas_bras["("] - mas_bras[")"])

str_temp = "Предскажите погоду: \n 1 - ясно \n 2 - пасмурно \n 3 - дождь \n"    
chek_input()

