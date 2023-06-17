def polind():
    str = input(f"Введите слово: ")
    str_revers = ''.join(reversed(str))
    if str == str_revers:
        print('True')
    else:
        print('False')

polind()

#Обьяснение: в функции мы принимает слово, и при помощи reversed переворачивает его, а при помощи join превращаем в строку.
#Дальше просто делаем проверку через условия.