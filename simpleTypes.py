# Практика числа
v = int(input('Введите число от 1 до 10: '))
a = v + 10
print(f'Число {a} на 10 больше введенного {v}')

# Практика строки
name = input('Введите ваше имя: ')
name = name.upper()
print('Привет, {}! Как дела?'.format(name))

# Практика приведение типов
print(float('1')) # 1.0
#print(int('2.5')) # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1)) # True
print(bool('')) # False
print(bool(0)) # False

# Приветствие
name = 'Денис'
print(name)

# Информация о пользователе
user_info = {'first_name': 'Денис', 'last_name': 'Щербатюк'}
print(user_info['first_name'])
print(user_info['last_name'])