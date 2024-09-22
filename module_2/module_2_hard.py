# student: Andrey Jaroslavtsev


def get_password(n):
    result = []
    first_num = []
    for num in range(1, 21):
        for j in range(1, 21):
            if n % (num + j) == 0:
                first_num.append(num)
                if not j in first_num:
                    result.append([num, j])
    return ''.join(''.join(str(c) for c in lst) for lst in result)


n = int(input("Введите число от 3 до 20: "))
result_ = get_password(n)
print(f'Ваш пароль: {result_}')


def test():
    for i in range(3, 21):
        pass_ = get_password(i)
        print(f'{i} - {pass_}')

# test()
