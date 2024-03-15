from django.db import models

class TaskData(models.Model):
    AssignedID=models.IntegerField(primary_key = True)
    TaskID=models.ForeignKey('TaskInformation', on_delete=models.CASCADE)
    AssignedTo=models.ForeignKey('Users',related_name="Assigned",on_delete=models.CASCADE)
    PriorityID=models.ForeignKey('Priority',on_delete=models.CASCADE)
    Status=Status = models.ForeignKey('Status',on_delete=models.CASCADE)
    DueDate=models.DateField()