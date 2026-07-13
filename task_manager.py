import json 
class Task:
    def __init__(self,id,title):
        self.id = id
        self.title = title
        self.status = False
    
    def change_stat(self):
        self.status = not self.status
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'status': self.status}

class Task_manager:
        
        def save(self):
            with open('/home/tim/py_project/ts_mn.json','w',encoding= 'utf-8') as f:
                json.dump([task.to_dict() for task in self.tasks] ,f)

        def __init__(self):
            self.tasks = []

        def show (self):
            for i in self.tasks:
                print (f'{i.id}: {i.title} = {i.status}')
        
        def delete (self,id):
            for i in self.tasks:
                if id == i.id:
                    return self.tasks.remove(i)

        def add (self,id,title):
            task = Task(id,title)
            self.tasks.append(task)
        
        def change_status (self,id):
            for i in self.tasks:
                if id == i.id:
                    return i.change_stat()
        
        def load(self):
            with open('/home/tim/py_project/task_manager.json','r',encoding= 'utf-8') as f:
                load = json.load(f)
                for i in load:
                    self.tasks.append(Task(i['id'], i['title']))
                    self.tasks[-1].status = i['status']
task = Task_manager()
task.change_status(1)
task.delete(4)
task.load()
task.show()
task.save() 