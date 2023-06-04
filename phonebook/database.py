import view
# Добавляет в файл новую запись
def add_dat(data):
    with open("database.txt", "a", encoding='utf-8') as file:
        file.writelines(data)
    print("Телефонная книга обновлена.")
# Ищет информацию в файле
def search_name(datа):
    with open("database.txt", "r", encoding='utf-8') as file:
        res = file.readlines()
        flag = False
        for i in res:
            if datа in i:
                print(i)
                flag = True
        if flag == False:
            print("Ненайдено")
# Изменяет информацию из файла
def edit_name(datа):
    with open("database.txt", "r", encoding='utf-8') as file:
        res = file.readlines()
        flag = False
        index = 0
        for i in res:
            if datа in i:
                index = res.index(i)
                flag = True
        if flag == False:
            print("Ненайдено")
    res[index] = view.man()
    with open("database.txt", "w", encoding='utf-8') as f:
        f.writelines(res)

# Удаляет информацию из файла
def delete_name(data):
    with open("database.txt", "r", encoding='utf-8') as file:
        res = file.readlines()
        flag = False
        index = 0
        for i in res:
            if data in i:
                index = res.index(i)
                flag = True
        if flag == False:
            print("Ненайдено")
    res.pop(index)
    with open("database.txt", "w", encoding='utf-8') as f:
        f.writelines(res)
