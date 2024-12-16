 # СЛОВАРИ И МНОЖЕСТВА
my_dict = {'Иван':36, 'Константин': 77, 'Ольга': 41}
my_dict ['Иван'] = 36
print(my_dict ['Иван'])
my_dict['Антон'] = 50
print(my_dict)
my_dict ['Глеб'] = 28
my_dict ['Артём'] = 42
print(my_dict)
del my_dict ['Антон']
print(my_dict)
# МНОЖЕСТВА
my_set = {1, 2, 2, 3, 3, 3, 4, 5, 'Max', 'Max'}
print(my_set)
my_set.update({'Антон', 'Глеб'})
print(my_set)
my_set.discard(1)
print(my_set)