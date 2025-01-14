import json
import pathlib
import sqlite3

class Task:
    def __init__(self,id=0, completed=False,content="",section=0,due_date="",should_repeat="", delete_on_complete=True):
        self.id = id
        self.content = content
        self.section = section
        self.due_date = due_date
        self.should_repeat = should_repeat
        self.completed = completed
        self.delete_on_complete = delete_on_complete

    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self, tasks=[],sections=[],next_id=0):
        self.tasks=tasks
        self.sections=sections
        self.next_id=next_id

    def add_task(self,completed,content,section,due_date,should_repeat,delete_on_complete):
        self.tasks.append(Task(self.next_id,False,content,section,due_date,should_repeat,delete_on_complete))

    def remove_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)

    def get_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task

    def get_tasks_by_section(self, section):
        return [task for task in self.tasks if task.section == section]

    def get_tasks(self):
        return self.tasks

    def edit_task(self, id, content, section, due_date, should_repeat, delete_on_complete):
        for task in self.tasks:
            if task.id == id:
                task.content = content
                task.section = section
                task.due_date = due_date
                task.should_repeat = should_repeat
                task.delete_on_complete = delete_on_complete

    def add_section(self, section):
        if section not in self.sections:
            self.sections.append(section)
        else:
            return False

    def remove_section(self, section_id):
        self.sections.pop(section_id)

    def edit_section(self, section_id, new_section):
        self.sections[section_id] = new_section

    def read_data_from_tmanager_file(self, path_to_vault):
        dotlifekeeper_path = path_to_vault + "/.lifekeeper"
        tmanager_conn = sqlite3.connect(dotlifekeeper_path + "/tmanager.db")
        cursor = tmanager_conn.cursor()
        
        

    def create_tmanager_file(self, path, tmanager_name):
        try:
            pathlib.Path(path + "/" + tmanager_name).mkdir(parents=True, exist_ok=False)
            pathlib.Path(path + "/" + tmanager_name + "/.lifekeeper").mkdir(parents=True, exist_ok=False)
            dotlifekeeper_path = path + "/" + tmanager_name + "/.lifekeeper"
            tmanager_conn = sqlite3.connect(dotlifekeeper_path + "/tmanager.db")
            cursor = tmanager_conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sections (
            section_name TEXT PRIMARY KEY)''')
            cursor.execute('''CREATE IF NOT EXISTS Tasks (
            task_name TEXT,
            task_id INTEGER,
            section_id INTEGER)''')
            

            
        except FileExistsError:
            return False

    def write_data_to_tmanager_file(self, path_to_tmanager):
        tasks_dict = [task.__dict__ for task in self.tasks]
        with open(path_to_tmanager + "/.lifekeeper/tmanager.json", "w") as f:
            json.dump({"tasks": tasks_dict, "sections": self.sections, "next_id": self.next_id}, f)
