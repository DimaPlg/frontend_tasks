import datetime


def greeting_day_time(time):
    if 4 < time < 11.01:
        print('Good morning')
    elif 11 < time < 15.01:
        print('Good day')
    elif 15 < time < 23.01:
        print('Good evening')
    else:
        print('Good night')

def cul(a,b,c):
    print(a+b*c**2)

time_h = int(input('Enter hour:'))
time_m = int(input('Enter minuet between 1 and 60:'))

time = time_h + time_m * (5/3)*(1/100)
greeting_day_time(time)

date = datetime.datetime.today()
date = date.strftime('%H:%M')
time = int(date[0:2]) + int(date[3:]) * (5/3)*(1/100)
greeting_day_time(time)

cul()