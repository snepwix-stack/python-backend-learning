from services import add_task, delete_task, delete_all_tasks, show_tasks


def show_menu():
    print(
        "1. Добавить задачу \n2. Показать все задачи \n3. Удалить задачу \n4. Удалить все задачи\n5. Выход"
    )
    choice = input("Выберите операцию: ")
    return choice


while True:
    choice = show_menu()
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        delete_all_tasks()
    elif choice == "5":
        break
