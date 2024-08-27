my_dict={'Andrey':1985,'Anton': 1990,"Djon": 1995 }
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Anna','имя не найдено'))
my_dict.update({'Nina':1990,'Liza': 1994})
print(my_dict)
del my_dict['Andrey']
print(my_dict)

my_set={1,2,3,5,6,"Count",7,1,2,3,7,"Apple","Count","Apple"}
print(my_set)
my_set.update({4.1,8})
print(my_set)
my_set.remove(7)
print(my_set)
