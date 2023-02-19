import notes

def main():
    while True:
        print('\nВыберите действие:\n1 - добавить заметку\n2 - изменить заметку\n3 - удалить заметку\n4 - вывести список заметок\n5 - просмотреть заметку\n0 - выход')
        choice = input()
        if choice == '1':
            notes.add_note()
        elif choice == '2':
            notes.edit_note()
        elif choice == '3':
            notes.delete_note()
        elif choice == '4':
            notes.list_notes()
        elif choice == '5':
            notes.view_note()
        elif choice == '0':
            break
        else:
            print('Некорректный ввод')

if __name__ == '__main__':
    main()
