
from Management.DAL.Entities import *


def Read(Table):
    if Table=='Users':
        return Users.objects.all()
    elif Table == 'TaskInformation':
        return  TaskInformation.objects.all()
    elif Table == 'TaskData':
        return  TaskData.objects.all()
    elif  Table =='Comments':
        return Comments.objects.all()
    elif Table == 'Priority':
        return Priority.objects.all()
    elif  Table == "Status":
        return Status.objects.all()
    else:
        return None
    
def addUser(User):
    Users.objects.create(**User)

def addTask(Task):
    TaskInformation.objects.create(**Task)

def Update(data,pk):
    TaskInformation.objects.filter(TaskID=pk).update(**data)

def UpdateData(pk,data):
    TaskData.objects.filter(TaskID=pk).update(**data)
    TaskInformation.objects.filter(TaskID=pk).update(**data)

def CommentEntry(comment):
    Comment=Comments.objects.create(**comment)

def addAssign(Assign):
    data=TaskData.objects.create(**Assign)


