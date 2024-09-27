# student: Andrey Jaroslavtsev


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1)
print_params(1, 'string')
print_params(2, 'string_2', False)
print_params(3, 'string_3', False)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = ['(•‿•)', False, 16.2]
values_dict = {'a':'test_str', 'b':10, 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)