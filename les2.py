
def sep_str(seporated_str):
    dial_list = seporated_str.split('/')
    count = 0
    for i in dial_list:
        if count % 2 == 0:
            print(f"\"{i}?\"")
            count += 1
            continue
        print(f"\"{i}\"")
        count += 1

def botle_v(money, cost):
    if cost > money:
        return 0
    return money//cost

def money_in_poc(money_poc, price):
    return money_poc - botle_v(money_poc, price)* price

def lost_money(pols_money, botl_pric):
    return pols_money - money_in_poc(pols_money, botl_pric)
    
str_in = 'Я в магаз, надо чего/Да, давай винца/Ок, мож закуски/Не, так бухнем'
sep_str(str_in)
mon = float(input("Сколько денег есть у пола: "))
pr = float(input("Цена ботля: "))   
botl = int(botle_v(mon, pr))
pol_lost = "%.2f" % lost_money(mon, pr)
pol_have = "%.2f" % money_in_poc(mon, pr)
if botl == 0:
    print("Похоже Пол будет ночевать на улице")
else:
    print(f"Пол решил споить девушку {botl} бутылками вина")
print(f"Это будет ему стоить {pol_lost}")
print(f"Полу придется жить до следующей зп на {pol_have}")

i = True
s = 10

print(s/i)
