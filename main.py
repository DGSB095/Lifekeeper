from task import *

sections = ["Buy milk", "watch arcane", "idk", "BRUH", "EHM Rust is better"]
tmanager = TaskManager([], sections, 0, [])

def add_new_task(sections):
    content = input("Введите описание задачи")
    print("Выберите раздел:")
    for index, section in enumerate(sections, 1):
        print(f"{index}. {section}")
    section = int(input("Введите номер раздела (или пустым, если нет): "))
    due_date = input("Установить дату выполнения (ДД.ММ.ГГГГ) или оставить пустым: ")
    should_repeat = input("Повторять задачу? (нет/каждые 3 дня): ")
    tmanager.add_task(False, content, section, due_date, should_repeat)

def show_tasks():
    tasks = tmanager.get_tasks()
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task.content} {f'({tmanager.sections[task.section - 1]}) ' if task.section != 0 else ''}")



while True:

    print("""=========================
      TASK-TRACKER
=========================
1. Добавить задачу
2. Просмотреть задачи
3. Редактировать задачу
4. Удалить задачу
5. Управление разделами
7. Выполнить задачу
7. Выход
Выберите опцию (1-6):""")
    option = int(input())
    match option:
        case 7:
            break
        case 6:
            print("Выполнить задачу")
        case 5:
            print("Управление разделами")
        case 4:
            print("Удалить задачу")
        case 3:
            print("Редактировать задачу")
        case 2:
            show_tasks()
        case 1:
            add_new_task(sections)