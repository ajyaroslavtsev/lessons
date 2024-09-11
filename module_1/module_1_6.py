# student: Andrey Jaroslavtsev


my_dict = {
    "Ivan": 1990,
    "Maria": 1985,
    "Alexander": 1980,
}
print('Dict:',my_dict)
print('Existing value:',my_dict['Ivan'])
print('Not existing value:',my_dict.get('Anton'))
my_dict.update({"Sasha": 1984, "Dasha": 1995})
age_Sasha = my_dict.pop('Sasha')
print("Deleted value:",age_Sasha)
print('Modified dictionary:',my_dict,'\n')

my_set = {1, 2.5, 'Hello', (1, 2), True, 1}
print('Set:',my_set)
my_set.add('Vasia')
my_set.add(3.14)
my_set.discard('Vasia')
print('Modified set:',my_set)
