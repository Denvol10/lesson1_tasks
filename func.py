# Функции задание 1
def get_summ(one, two, delimiter='&'):
	one = str(one)
	two = str(two)
	return one + delimiter + two
text = get_summ('Learn', 'python')
print(text.upper())

# Функции задание 2
def format_price(price):
	price = int(price)
	return f'Цена: {price} руб.'
price1 = format_price(52.64)
print(price1)