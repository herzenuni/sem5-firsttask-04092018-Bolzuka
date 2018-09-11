# Практичское задание 0
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Напишите программу, в которой пользователь вводит число от 0 до 9 включительно,а программа выводит название введённого числа, 
# а если ? второй входной аргумент ? type имеет значение bin, oct, hex, то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму. 
# Предусмотреть проверку корректности введённого пользователем значения. При реализации должны использоваться декораторы. При реализации должны использоваться декораторы (но можно обойтись и без них). Предусмотрите обработку исключительных ситуаций. Напишите тесты с использованием assert.

# bin(x) - преобразование целого числа в двоичную строку.
# oct(х) - преобразование целого числа в восьмеричную строку. 
# hex(х) - преобразование целого числа в шестнадцатеричную строку.




def print_number_and_word(number, t=''):

    if (number == 0):
        print("\n Ноль")
    elif (number == 1):
        print("\n Один")
    elif (number == 2):
        print("\n Два")
    elif (number == 3):
        print("\n Три")
    elif (number == 4):
        print("\n Четыре")
    elif (number == 5):
        print("\n Пять")
    elif (number == 6):
        print("\n Шесть")
    elif (number == 7):
        print("\n Семь")
    elif (number == 8):
        print("\n Восемь")
    elif (number == 9):
        print("\n Девять")
    else:
        print("\n Такой цифры нет")

    if t == 'bin':
        print(bin(number))
    elif t == 'oct':
        print(oct(number))
    elif t == 'hex':
        print(hex(number))
      
print_number_and_word(0,'bin')
# вводим значение

def print_number_and_word():
  assert 0 == 'Ноль', 'Название цифры не верно'
  assert 1 == 'Один', 'Название цифры не верно'
  assert 2 == 'Два', 'Название цифры не верно'
  assert 3 == 'Три', 'Название цифры не верно'
  assert 4 == 'Четыре', 'Название цифры не верно'
  assert 5 == 'Пять', 'Название цифры не верно'
  assert 6 == 'Шесть', 'Название цифры не верно'
  assert 7 == 'Семь', 'Название цифры не верно'
  assert 8 == 'Восемь', 'Название цифры не верно'
  assert 9 == 'Девять', 'Название цифры не верно'
  assert (7,'bin') == ('Семь', '0b111'), 'Название цифры не верно'
  assert (1,'oct') == ('Один', '0o1'), 'Название цифры не верно'
  assert (2,'hex') == ('Два', '0x2'), 'Название цифры не верно'


  
