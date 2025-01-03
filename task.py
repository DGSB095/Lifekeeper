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
