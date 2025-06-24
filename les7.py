#Given a string s consisting only of characters a, b and c.
#Return the number of substrings containing at least one
#occurrence of all these characters a, b and c.

def jok(str_test):
    count = 0
    len_s = len(str_test)
    res = 0
    for i in range(1, len_s - 1):
        if (str_test[i - 1] != str_test[i] and str_test[i - 1] != str_test[i]) and str_test[i - 1] != str_test[i + 1]:
            count += 1
    for i in range(count, 0 , -1):
        res += len_s - 2
        len_s -= 1       
    return res 

str1 = "abcabc"
print(jok(str1))
print(jok("aaabc"))
print(jok('"ababbbc"'))


def is_number(num):
    if is_float(num) or is_int(num) == True:
        return True
    return False

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def is_int(num):
    return num.isdigit()

def input_num():
    num_f = True
    while num_f:
        x1 = input('Enter begin number: ')
        x2 = input('Enter last number: ')
        if is_number(x1) and is_number(x2):
            return chek_enter_num(int(float(x1)), int(float(x2)))
        print('May be you would like to try again?')

def chek_enter_num(num1, num2):
    if num1 > num2 - 1:
        return sum_num_between(num2, num1)
    return sum_num_between(num1, num2)

def sum_num_between(x1, x2):
    res = 0
    while x1 < x2:
        res +=x1
        x1 +=1
    return res



#print(f'{input_num()}')   


    
    
