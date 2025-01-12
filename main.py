from task import *

sections = ["Buy milk", "watch arcane", "idk", "BRUH", "EHM Rust is better"]
tmanager_path = ""
tmanager = TaskManager([], sections, 0)

def add_new_task(sections):
    content = input("Введите описание задачи: ")
    print("Выберите раздел: ")
    for index, section in enumerate(tmanager.sections, 1):
        print(f"{index}. {section}")
    section = int(input("Введите номер раздела (или пустым, если нет): "))
    due_date = input("Установить дату выполнения (ДД.ММ.ГГГГ) или оставить пустым: ")
    should_repeat = input("Повторять задачу? (нет/каждые 3 дня): ")
    delete_on_complete = input("Удалить задачу после завершения? (Y/N): ")
    if delete_on_complete.lower() == "y":
        tmanager.add_task(False, content, section, due_date, should_repeat,True)
    else:
        tmanager.add_task(False, content, section, due_date, should_repeat,False)
    tmanager.write_data_to_tmanager_file(tmanager_path)


def show_tasks():
    tasks = tmanager.get_tasks()
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task.content} {f'({tmanager.sections[task.section - 1]}) ' if task.section != 0 else ''}{f'- до {task.due_date}' if task.due_date != '' else ''} {f'- повторять каждые {task.should_repeat} дней' if task.should_repeat != '' else ''} {f'- выполнено' if task.completed else ''}")

def delete_task():
    show_tasks()
    tasks = tmanager.get_tasks()
    id = int(input("Введите номер задачи для удаления: "))
    for index, task in enumerate(tasks, 1):
        if index == id:
            id = task.id
    tmanager.remove_task(id)

def complete_task():
    show_tasks()
    id = int(input("Введите номер задачи для завершения: "))
    tasks = tmanager.get_tasks()
    for index, task in enumerate(tasks, 1):
        if index == id:
            id = task.id
    task = tmanager.get_task(id)
    task.complete()
    if task.delete_on_complete:
        tmanager.remove_task(id)

def edit_task():
    tasks = tmanager.get_tasks()
    show_tasks()
    id = int(input("Введите номер задачи для редактирования: "))
    for index, task in enumerate(tasks, 1):
        if index == id:
            id = task.id
    content = input("Введите описание задачи: ")
    print("Выберите раздел: ")
    while True:
        for index, section in enumerate(sections, 1):
            print(f"{index}. {section}")
        section = int(input("Введите номер раздела (или пустым, если нет): "))
        if len(sections) < section:
            print("Введите корректный номер раздела.")
        else:
            break
    due_date = input("Установить дату выполнения (ДД.ММ.ГГГГ) или оставить пустым: ")
    should_repeat = input("Повторять задачу? (нет/каждые 3 дня): ")
    delete_on_complete = input("Удалить задачу после завершения? (Y/N): ")
    if delete_on_complete.lower() == "y":
        tmanager.edit_task(id, content, section, due_date, should_repeat, True)
    else:
        tmanager.edit_task(id, content, section, due_date, should_repeat, False)

def sections_control_menu():
    while True:
        print("""=========================
           LIFEKEEPER
   Управление разделами
=========================
1. Добавить раздел
2. Просмотреть разделы
3. Удалить раздел
4. Редактировать раздел
5. В меню
Выберите опцию (1-5):""")
        option = int(input())
        match option:
            case 1:
                section_name = input("Введите имя раздела: ")
                tmanager.add_section(section_name)
            case 2:
                for index, section in enumerate(tmanager.sections, 1):
                    print(f"{index}. {section}")
            case 3:
                for index, section in enumerate(sections, 1):
                    print(f"{index}. {section}")
                section_id = int(input("Введите номер раздела для удаления: "))
                if section_id > len(sections) or section_id < 1:
                    print("Введите корректный номер раздела.")
                else:
                    tmanager.remove_section(section_id - 1)
            case 4:
                print("WORK IN PROGRESS")
            case 5:
                break
        tmanager.write_data_to_tmanager_file(tmanager_path)

def main_menu():
    while True:

        print("""=========================
          LIFEKEEPER
=========================
1. Добавить задачу
2. Просмотреть задачи
3. Редактировать задачу
4. Удалить задачу
5. Управление разделами
6. Выполнить задачу
7. Выход
Выберите опцию (1-7): """)
        option = int(input())
        match option:
            case 7:
                break
            case 6:
                complete_task()
            case 5:
                sections_control_menu()
            case 4:
                delete_task()
            case 3:
                edit_task()
            case 2:
                show_tasks()
            case 1:
                add_new_task(sections)

while True:
    print("""=========================
       LIFEKEEPER
=========================
Здравствуйте, пожалуйста выберите опцию:
1.Открыть tmanager
2.Создать tmanager
3.Выйти""")
    choice = input()
    match choice:
        case "1":
            tmanager_path = input("Введите путь к tmanager: ")
            tmanager.read_data_from_tmanager_file(tmanager_path)
            main_menu()
        case "2":
            tmanager_path = input("Введите путь к директории, где вы хотите создать новый tmanager: ")
            tmanager_name = input("Введите имя менеджера задач: ")
            tmanager.create_tmanager_file(tmanager_path, tmanager_name)
        case "3":
            break
        case _:
            print("Please choose an option")
print(tmanager_path)