from optparse import Option


class Task:
    def __init__(self,id=0, completed=False,content="",section=0,due_date="",should_repeat=""):
        self.id = id
        self.content = content
        self.section = section
        self.due_date = due_date
        self.should_repeat = should_repeat
        self.completed = completed
    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self, tasks=[],sections=[],next_id=0, removed_ids=[]):
        self.tasks=tasks
        self.sections=sections
        self.next_id=next_id
        self.removed_ids = removed_ids

    def add_task(self,completed,content,section,due_date,should_repeat):
        self.tasks.append(Task(completed,content,section,due_date,should_repeat))

    def remove_task(self, id):
        self.removed_ids.append(id)
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

    def edit_task(self, id, content, section, due_date, should_repeat):
        for task in self.tasks:
            if task.id == id:
                task.content = content
                task.section = section
                task.due_date = due_date
                task.should_repeat = should_repeat


