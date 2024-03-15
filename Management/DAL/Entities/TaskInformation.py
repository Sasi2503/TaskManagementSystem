from django.db import models

class TaskInformation(models.Model):
    TaskID=models.IntegerField(primary_key = True)
    Title=models.CharField(max_length=100,null=False)
    Description=models.TextField()
    StartDate = models.DateTimeField(auto_now_add=True)
    DueDate=models.DateField()
    Assignedby=models.ForeignKey('Users',on_delete=models.CASCADE)
    Status=Status = models.ForeignKey('Status',on_delete=models.CASCADE)
    PriorityID=models.ForeignKey('Priority',on_delete=models.CASCADE)
    

