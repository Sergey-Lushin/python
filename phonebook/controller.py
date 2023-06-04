import view
import database

def main():
    while True:
        ask = view.user_input()
        print(ask)
        if ask == 1:
            data = view.man()
            database.add_dat(data)
        elif ask == 2:
            data = view.search_man_name()
            database.search_name(data)
        elif ask == 3:
            data = view.edit_man_name()
            database.edit_name(data)
        elif ask == 4:
            data = view.delete_man_name()
            database.delete_name(data)
        elif ask == 6:
            break

main()