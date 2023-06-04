def user_input():
    ask = int(input("Выберите ниже: \n1 - записать пользователя \n2 - поиск пользователя \n3 - изменить пользоватея \n4 - удалить пользователя \n6 - выход\n"))
    return ask

def man():
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    father = input("Введите отчество: ")
    date = input("Введите дату рождения: ")
    telephone = input("Введите номер телефона: ")
    data = name+"; "+family+"; "+father+"; "+ date+"; "+telephone+";\n"
    print(data)
    return data

def search_man_name():
    search = input("Введите фамилию: ")
    return search

def edit_man_name():
    edit = input("Введите фамилию: ")
    return edit

def delete_man_name():
    delete = input('Введите фимилию: ')
    return delete
