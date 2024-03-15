from django.db import models
class Comments(models.Model):
    CommentID=models.AutoField(primary_key=True)
    Content=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    UserID=models.ForeignKey('Users', on_delete=models.SET_NULL, blank=True, null=True)
    TaskID=models.ForeignKey('TaskInformation',on_delete=models.CASCADE)
