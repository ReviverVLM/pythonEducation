# 4th programm
print('123.456')
print(float('123.456'))
print(float('123.456')*10)
print(float('123.456')*10 % 10)
print(int(float('123.456')*10 % 10))
# или
print('123.456')
print(float('123.456'))
print(int(float('123.456')))
print(float('123.456')*10 - int(float('123.456'))*10)
print(int(float('123.456')*10 - int(float('123.456'))*10))

# или
print(int(float('123.456')*10 % 10//1))
# или
a = '123.456'
a = float(a)
a = a * 10 % 10
a = int(a)
print(a)
