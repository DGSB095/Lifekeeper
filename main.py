from task import *

sections = ["suck dick", "Buy milk", "watch arcane", "idk", "BRUH", "EHM Rust is better"]
tmanager = TaskManager([], sections, 0, [])

def add_new_task(sections):
    content = input("Введите описание задачи")
    print("Выберите раздел:")
    for index, section in enumerate(sections, 1):
        print(f"{index}. {section}")
    section = int(input("Введите номер раздела (или пустым, если нет): "))
    due_date = input("Установить дату выполнения (ДД.ММ.ГГГГ) или оставить пустым: ")
    should_repeat = input("Повторять задачу? (нет/каждые 3 дня): ")
    delete_on_complete = input("Удалить задачу после завершения? (Y/N): ")
    if delete_on_complete == "Y":
        tmanager.add_task(False, content, section, due_date, should_repeat,True)
    else:
        tmanager.add_task(False, content, section, due_date, should_repeat,False)


def show_tasks():
    tasks = tmanager.get_tasks()
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task.content} {f'({tmanager.sections[task.section - 1]}) ' if task.section != 0 else ''}{f'- до {task.due_date}' if task.due_date != '' else ''} {f'- повторять каждые {task.should_repeat} дней' if task.should_repeat != '' else ''} {f'- выполнено' if task.completed else ''}")

def delete_task():
    show_tasks()
    id = int(input("Введите номер задачи для удаления: "))
    tmanager.remove_task(id)

def complete_task():
    show_tasks()
    id = int(input("Введите номер задачи для завершения: "))
    task = tmanager.get_task(id)
    task.complete()
    if task.delete_on_complete:
        tmanager.remove_task(id)

def edit_task():
    show_tasks()
    id = int(input("Введите номер задачи для редактирования: "))
    content = input("Введите описание задачи")
    print("Выберите раздел:")
    for index, section in enumerate(sections, 1):
        print(f"{index}. {section}")
    section = int(input("Введите номер раздела (или пустым, если нет): "))
    due_date = input("Установить дату выполнения (ДД.ММ.ГГГГ) или оставить пустым: ")
    should_repeat = input("Повторять задачу? (нет/каждые 3 дня): ")
    delete_on_complete = input("Удалить задачу после завершения? (Y/N): ")
    if delete_on_complete == "Y":
        tmanager.add_task(False, content, section, due_date, should_repeat, True)
    else:
        tmanager.add_task(False, content, section, due_date, should_repeat, False)

while True:

    print("""=========================
      TASK-TRACKER
=========================
1. Добавить задачу
2. Просмотреть задачи
3. Редактировать задачу
4. Удалить задачу
5. Управление разделами
6. Выполнить задачу
7. Выход
Выберите опцию (1-7):""")
    option = int(input())
    match option:
        case 7:
            break
        case 6:
            complete_task()
        case 5:
            print("WORK IN PROGRESS ")
        case 4:
            delete_task()
        case 3:
            edit_task()
        case 2:
            show_tasks()
        case 1:
            add_new_task(sections)
