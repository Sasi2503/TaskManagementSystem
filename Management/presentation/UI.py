from django.shortcuts import render,redirect,HttpResponse
from Management.presentation.ViewModels.TaskInformationviewmodel import TaskForm
from Management.presentation.ViewModels.registrationviewmodel import RegisterForm
from Management.presentation.ViewModels.loginviewmodel import LoginForm
from Management.presentation.ViewModels.assignedviewmodel import assignedviewmodel
from Management.presentation.ViewModels.CommentViewModel import CommentViewModel
from Management.presentation.ViewModels.TaskViewModel import TaskViewModel
from Management.presentation.ViewModels.Updateviewmodel import UpdateTaskForm,UpdateStatusForm
from Management.presentation.ViewModels.addcommentsviewmodel import CommentsForm
from Management.presentation.ViewModels.assignedtasksviewmodel import assignedForm
from Management.Services.ServiceModels.UsersServices import UsersServices
from Management.Services.ServiceModels.TaskInformationServices import TaskInformationServices
from Management.Services.ServiceModels.TaskDataServices import TaskDataServices
from ..Services.Services import *
from django.core.exceptions import ValidationError

def dashboard(request):
    return render(request, 'Templates/Homepage.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            user=UsersServices(
                UserID=None,
                firstname=cleaned_data['firstname'],
                lastname=cleaned_data['lastname'],
                UserName=cleaned_data['UserName'],
                Password=cleaned_data['Password'],  
            )
            

            InsertUser(user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Templates/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['UserName']
            password = form.cleaned_data['Password']
        
            user = Users.objects.filter(UserName=username,Password=password).first()
            if user:
                user_id = user.UserID
                request.session['user_id'] = user_id
                return redirect('TaskManagement')  
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'login.html', {'error_message': error_message})
        
    else:
        form = LoginForm()  
    return render(request, 'Templates/login.html', {'form': form})

def Home(request):
    
    tasklist=TaskDetails()
    assignedlist=TaskDataDetails()
    Task_view=[]
    for task in tasklist:
        task_vm = TaskViewModel(
            taskID=task.TaskID,
            Assignedby=task.Assignedby,  
            Title=task.Title,  
            Description=task.Description,  
            DueDate=task.DueDate,  
            Status=task.Status,  
            Priority=task.Priority,
            
        ) 
        Task_view.append(task_vm)
    return render(request,'Templates/TaskManagement.html',{'form':Task_view})



def addTask(request):
    user_id = request.session.get('user_id')
    user=viewID(user_id,'Users')
    # data=TaskData.objects.select_related('TaskID')
    # for i in data:
    #     if i.AssignedTo.firstname=='Sasidhar':
    #         print(i.AssignedTo.firstname)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user=viewID(user_id,'Users')
            priority= viewID(cleaned_data['PriorityID'],'Priority')
            status= viewID(cleaned_data['Status'],'Status')
            
            task = TaskInformationServices(
                TaskID=None,
                Title=cleaned_data['Title'],
                Description=cleaned_data['Description'],
                StartDate=None,
                DueDate=cleaned_data['DueDate'],
                Assignedby=user, 
                Status=status,
                Priority=priority,
            )
            InsertTask(task)
            return redirect('TaskManagement')
    else:
        form = TaskForm()
    return render(request, 'Templates/CreateTask.html', {'form': form})

def updateTask(request,pk):
    data=viewID(pk,"TaskInformation")
    userid=request.session.get('user_id')
    user=viewID(userid,'Users')
    if request.method == 'POST':
        taskform=UpdateTaskForm(request.POST)
        statusform=UpdateStatusForm(request.POST)
        if  taskform.is_valid() and statusform.is_valid():
            task=taskform.cleaned_data
            data=statusform.cleaned_data
            priority= viewID(data['Priority'],'Priority')
            status= viewID(data['Status'],'Status')
            updatedtask=TaskInformationServices(
                TaskID=None,
                Title=task['Title'],
                Description=task['Description'],
                StartDate=None,
                DueDate=data['DueDate'],
                Assignedby=user, 
                Status=status,
                Priority=priority,
            )
            TaskUpdate(updatedtask,pk)
            return redirect('TaskManagement')
    else:
        taskform=UpdateTaskForm()
        statusform=UpdateStatusForm()
    return render(request, 'Templates/Update.html', {'task': taskform,'status':statusform,'data':data})



def UpdateStatus(request, pk):
    if request.method == 'POST':
        form =UpdateStatusForm(request.POST)
        
        if form.is_valid():
            form=form.cleaned_data
            status= viewID(form['Status'],'Status')
            priority= viewID(form['Priority'],'Priority')
            task = TaskDataServices(
                AssignedID=None,
                TaskID=None,
                AssignedTo=None,
                PriorityID=priority,
                Status=status,
                DueDate=form['DueDate'],
            )
            Statusupdate(task,pk)
            return redirect('TaskManagement')
        
    else:
        form =UpdateStatusForm()
    return render(request, 'Templates/UpdateStatus.html', {'form': form})


def assign(request, pk):
    task = viewID(pk,'TaskInformation')
    if request.method == 'POST':
        form = assignedForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # print(cleaned_data)
            assigned_users = form.cleaned_data['AssignedTo']
            priority= viewID(cleaned_data['PriorityID'],'Priority')
            status= viewID(cleaned_data['Status'],'Status')
            # print(assigned_users,priority,status)
            for user_id in assigned_users:
                user=viewID(user_id,'Users')
                
                try:
                    assigned_task = TaskDataServices(
                        AssignedID=None,
                        TaskID=task,
                        AssignedTo=None,
                        PriorityID=priority,
                        Status=status,
                        DueDate=cleaned_data['DueDate']
                    )
                    assignTask(assigned_task,user)
                except ValidationError as e:
                    form.add_error('AssignedTo', e)

            return redirect('TaskManagement')
    else:
        form = assignedForm()

    return render(request, 'Templates/Assign.html', {'form': form})

# def Tasks(request):
#     user_id = request.session.get('user_id')
#     user=viewID(user_id,'Users')
#     data=TaskData.objects.select_related('TaskID')
#     for i in data:
#         print(i.AssignedTo.firstname)
#     assignedlist=TaskDataDetails()
#     print(assignedlist[2].AssignedTo)
#     return render(request, 'mytasks.html',{'form':assignedlist})



def Tasks(request):
    user_id = request.session.get('user_id')
    
    assignedlist=TaskDataDetails(user_id)
    Task_view=[]
    for task in assignedlist:
        task_vm = assignedviewmodel(
            AssignedID=task.AssignedID,
            TaskID=task.TaskID,  
            AssignedTo=task.AssignedTo,  
            PriorityID=task.PriorityID,  
            Status=task.Status,  
            DueDate=task.DueDate,
            
        ) 
        Task_view.append(task_vm)
    return render(request,'Templates/mytasks.html',{'form':Task_view})

def AssignedTasks(request):
    assignedlist=TaskDataDetails()
    Task_view=[]
    for task in assignedlist:
        task_vm = assignedviewmodel(
            AssignedID=task.AssignedID,
            TaskID=task.TaskID,  
            AssignedTo=task.AssignedTo,  
            PriorityID=task.PriorityID,  
            Status=task.Status,  
            DueDate=task.DueDate,
            
        ) 
        Task_view.append(task_vm)
    return render(request,'Templates/AssignedTasks.html',{'form':Task_view})

def comments(request,pk):
    commentlist=CommentsDetails(pk)
    Comments=[]
    for data in commentlist:
        comment = CommentViewModel(
            TaskID = data.TaskID,
            comment=data.Content,
            Date = data.Date,
            UserID = data.UserID,
            
        ) 
        Comments.append(comment)

    user_id = request.session.get('user_id')
    user=viewID(user_id,'Users')
    # print(user_id)
    # print(user)
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if  form.is_valid():
            comment=CommentsServices(
                CommentID=None,
                Content=form.cleaned_data['content'],
                Date=None,
                UserID=user,
                TaskID=None,
            )
            addcomment(comment,pk)
            return redirect('TaskManagement')
    else:
        form=CommentsForm()
    return render(request, "Templates/comments.html", {'form':form,'Content':Comments})
