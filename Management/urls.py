from django.urls import path
from Management.presentation import UI
urlpatterns = [
    path('',UI.dashboard,name='Dashboard'),
    path('register/', UI.register, name='register'),
    path('login/', UI.user_login, name='login'),
    path('HomePage/',UI.Home,name='TaskManagement'),
    path('CreateTask/', UI.addTask, name='CreateTask'),
    path('mytasks', UI.Tasks, name='mytask'),
    path('alltasks/', UI.AssignedTasks, name='allAssignedTasks'),
    path('update/<int:pk>',UI.updateTask,name="update"),
    path('updatestatus/<int:pk>',UI.UpdateStatus,name="updatestatus"),  # update task status
    path('assigntask/<int:pk>',UI.assign,name="AssignTask"),
    path('comments/<int:pk>',UI.comments,name="Comments"),     
]
