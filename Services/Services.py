from Management.Services.ServiceModels.TaskInformationServices import TaskInformationServices
from Management.Services.ServiceModels.UsersServices import UsersServices
from Management.Services.ServiceModels.PriorityServices import PriorityServices
from Management.Services.ServiceModels.TaskDataServices import TaskDataServices
from Management.Services.ServiceModels.StatusServices import StatusServices
from Management.Services.ServiceModels.CommentsServices import CommentsServices
from Management.DAL.repository import *



def InsertUser(user):
    UserEntry = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'UserName': user.UserName,
        'Password': user.Password,
    }
    addUser(UserEntry)

def InsertTask(Task):
    
    TaskEntry = {
        'Title': Task.Title,
        'Description': Task.Description,
        'DueDate': Task.DueDate,
        'Assignedby':Task.Assignedby,
        'Status': Task.Status,
        'PriorityID': Task.Priority,
        
    }
    addTask(TaskEntry) 

def TaskUpdate(Task,pk):
    update={
        'Title': Task.Title,
        'Description': Task.Description,
        'DueDate': Task.DueDate,
        'Assignedby':Task.Assignedby,
        'Status': Task.Status,
        'PriorityID': Task.Priority,
    }
    return Update(update,pk)

def Statusupdate(formdata,pk):
    update= {'Status': formdata.Status,
             'PriorityID':formdata.PriorityID,
             'DueDate':formdata.DueDate,
             
             }
    return UpdateData(pk,update)

def assignTask(Task,pk):
    AssignedTask = {
        'TaskID': Task.TaskID,
        'AssignedTo': pk,
        'PriorityID': Task.PriorityID,
        'Status': Task.Status,
        'DueDate': Task.DueDate,  
    }
    addAssign(AssignedTask)


def viewID(pk,form):
    if form=='Users':
        return  Users.objects.get(UserID=pk)
    elif form=='TaskInformation':
        return TaskInformation.objects.get(TaskID=pk)
    elif form=='Status':
        return  Status.objects.get(StatusID = pk)
    elif form== 'Priority':
        return Priority.objects.get(PriorityID = pk)
    else:
        return None

def addcomment(Comment,pk):
    taskid=viewID(pk,'TaskInformation')
    print()
    print(taskid)
    print()
    CommentAdded={'CommentID':None,
                 'TaskID':taskid,
                 'Content':Comment.Content,
                 'UserID':Comment.UserID,
                 }
    CommentEntry(CommentAdded)
    

def TaskDetails(TaskID=None):

    if TaskID is None:
        tasks=Read('TaskInformation')
        TaskServices=[]
        for task in tasks:
            tasksm=TaskInformationServices(
                TaskID=task.TaskID,
                Title=task.Title,
                Description=task.Description,
                StartDate=task.StartDate,
                DueDate=task.DueDate,
                Assignedby=task.Assignedby,
                Status=task.Status,
                Priority=task.PriorityID,
            )
            TaskServices.append(tasksm)
        return TaskServices
    else: 
        tasks = Read('TaskInformation').filter(pk=int(TaskID))
        TaskServices=[]
        for task in tasks:
            tasksm = TaskInformationServices(
                TaskID=task.TaskID,
                Title=task.Title,
                Description=task.Description,
                StartDate=task.StartDate,
                DueDate=task.DueDate,
                Assignedby=task.Assignedby,
                Status=task.Status,
                Priority=task.PriorityID,
        )
        TaskServices.append(tasksm)
        return TaskServices


def userDetails(UserID=None):

    if UserID is None:
        users=Read('Users')
        userServices=[]
        for user in users:
            usersm = UsersServices(
                UserID=user.UserID,
                UserName=user.UserName,
                firstname=user.firstname,
                lastname=user.lastname,
                Password=user.Password,
        )
            userServices.append(usersm)
        return userServices
    else: 
        users = Read('Users').select_related('TaskID')
        userServices=[]
        for user in users:
            usersm = UsersServices(
                UserID=user.UserID,
                UserName=user.UserName,
                firstname=user.firstname,
                lastname=user.lastname,
                Password=user.Password,
        )
        userServices.append(usersm)
        return userServices
    


def priorityDetails(PriorityID=None):

    if PriorityID is None:
        priority=Read('Priority')
        priorityservices=[]
        for data in priority:
            prioritysm = PriorityServices(
                PriorityID=data.PriorityID,
                PriorityName=data.PriorityName,
        )
            priorityservices.append(prioritysm)
        return priorityservices
    else: 
        priority = viewID(PriorityID,'Priority')
        priorityservices=[]
        for data in priority:
            prioritysm = PriorityServices(
                PriorityID=data.PriorityID,
                PriorityName=data.PriorityName,
        )
            priorityservices.append(prioritysm)
        return priorityservices
    


def statusDetails(StatusID=None):

    if StatusID is None:
        status=Read('Status')
        statusServices=[]
        for data in status:
            statusSm = StatusServices(
                StatusID=data.StatusID,
                Status=data.Status,
        )
            statusServices.append(statusSm)
        return statusServices
    else: 
        status=Read('Status').filter(pk=StatusID)
        statusServices=[]
        for data in status:
            statusSm = StatusServices(
                StatusID=data.StatusID,
                Status=data.Status,
        )
            statusServices.append(statusSm)
        return statusServices
    

def TaskDataDetails(AssignedID=None):

    if AssignedID is None:
        tasks=Read('TaskData')
        taskdataservices=[]
        for task in tasks:
            tasksm=TaskDataServices(
                AssignedID=task.AssignedID,
                TaskID=task.TaskID,
                AssignedTo=task.AssignedTo,
                PriorityID=task.PriorityID,
                Status=task.Status,
                DueDate=task.DueDate,
            )
            taskdataservices.append(tasksm)
        return taskdataservices
    else: 
        tasks = Read('TaskData').filter(AssignedTo=int(AssignedID))
        taskdataservices=[]
        for task in tasks:
            tasksm=TaskDataServices(
                AssignedID=task.AssignedID,
                TaskID=task.TaskID,
                AssignedTo=task.AssignedTo,
                Status=task.Status,
                PriorityID=task.PriorityID,
                DueDate=task.DueDate,
            )
            taskdataservices.append(tasksm)
        return taskdataservices

def CommentsDetails(task_id):
    tasks = Comments.objects.filter(TaskID=task_id)
    commentslist=[]
    for task in tasks:
        comment=CommentsServices(
            CommentID=task.CommentID,
            Content=task.Content,
            Date=task.Date,
            UserID=task.UserID,
            TaskID=task.TaskID,
        )
        commentslist.append(comment)
    return commentslist


