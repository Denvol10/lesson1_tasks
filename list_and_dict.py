# Задание списки
lst = [3, 5, 7, 9, 10.5]
print(lst)
lst.append('Python')
print(lst)
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst[2:5])
lst.remove('Python')
print(lst)

# Задание словари
weather = {'city': 'Moscow', 'temperature': '20'}
print(weather['city'])
weather['temperature'] = str(int(weather['temperature']) - 5)
print(weather)
print(weather.get('country'))
print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2019'
print(weather)
print(len(weather))