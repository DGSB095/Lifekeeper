def add_new_task(sections):
    content = input("Введите описание задачи")
    print("Выберите раздел:")
    for index, section in enumerate(sections, 1):
        print(f"{index}. {section}")
    section = int(input("Введите номер раздела (или пустым, если нет): "))

sections = ["Buy milk", "watch arcane", "idk", "BRUH", "EHM Rust is better"]
while True:

    print("""=========================
      TASK-TRACKER
=========================
1. Добавить задачу
2. Просмотреть задачи
3. Редактировать задачу
4. Удалить задачу
5. Управление разделами
6. Выход
Выберите опцию (1-6):""")
    option = int(input())
    match option:
        case 6:
            break
        case 5:
            print("Управление разделами")
        case 4:
            print("Удалить задачу")
        case 3:
            print("Редактировать задачу")
        case 2:
            print("Посмотреть задачи")
        case 1:
            add_new_task(sections)