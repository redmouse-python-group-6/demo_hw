# -*- coding: utf-8 -*-
def func1 (): 
	return u"Вам в детский сад"

def func2():
	return  u"Вам в школу"

print u"Общество в начале XXI века"
age=int(raw_input("Введите ваш возраст "))
if 0<=age<=7:
    print func1()
elif age<=18:
    print func2()
elif age<=25:
    print u"Вам в профессиональное учебное заведение"
elif age<=60:
    print u"Вам на работу"
elif age<=120:
    print u"Вам предоставляется выбор"
else:
    error = u"Ошибка! Это программа для людей!\n"
    print error*5