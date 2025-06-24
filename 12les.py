s_ex = 'example'
#print([e + '*' for e in s_ex])


[print('\n') if i == 11 and j == 5 else print('',end = '') if i == 11 else  print('') if j == 6 else print(f'{j + 5} x {i - 10} = {(i - 10)*(j + 5)}\t',end ='\t')if i > 10 else print(f'{j} x {i} = {i*j}\t',end ='\t')for i in range(1,21) for j in range(1,7)]

userLogs=["admin","student","teacher","HR","user"]
print(['newUser1' if i == "admin" else  'newUser2' if i == "student" else  'newUser3' if i == "user" else i for i in userLogs])
