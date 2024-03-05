phonebook = {'Ваня': 4098, 'Коля': 4139, 'Петя': 1489,}
# словарь
file = open('phonebook.txt', 'w', encoding = 'utf-8')
for key, value in phonebook.items():
	file.write(f'{key}, {value}\n')
file.close()

e = "test"
x = 0
control = 0
while control == 0:
    a = int(input("""0 - новый контакт
1 - просмотр книги
2 - поиск по имени
3 - поиск по номеру
4 - удаление записи    """))
    if a == 1:
        b = phonebook.keys()
        b = list(b)
        b.sort()
        for key in b:
            print(key +'-' +str(book[key]))
    elif a == 0:
        e = input("""Введите имя    """)
        x = int(input("""Введите номер    """))
        file = open('phonebook.txt', 'w', encoding = 'utf-8')
        book[e]= x
    elif a ==2:
        e = input("""Введите имя    """)
        if e in phonebook:
            print(phonebook[e])
        else:
            print("Контакта не существует")
    elif a == 3:
        x = int(input("""Введите номер    """))
        mirror = dict(zip(phonebook.values(), phonebook.keys()))
        if x in mirror:
            print(mirror[x])
        else:
            print("Контакта не существует")
    elif a == 4:
        e = input("""Введите имя    """)
        if e in phonebook:
            del phonebook[e]
        else:
            print("Такой записи не существует")
    else:
        print("ERROR")
        
        break