class Task:
    def __init__(self,completed=False,content="",section=0,due_date="",should_repeat=""):
        self.content = content
        self.section = section
        self.due_date = due_date
        self.should_repeat = should_repeat
        self.completed = completed

    def new(self,completed,content,section,due_date,should_repeat):
        self.content = content
        self.section = section
        self.due_date = due_date
        self.should_repeat = should_repeat
        self.completed = completed
        return self
