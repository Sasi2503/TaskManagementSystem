from django import forms
from datetime import date

class TaskForm(forms.Form):
    Title=forms.CharField(widget=forms.TextInput)
    Description = forms.CharField(widget=forms.Textarea,required=False)
    DueDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
    
    Status=forms.ChoiceField(choices=[(None, '---------'),(1,'Not Started'), (2, 'In Progress'), (3,'Completed')])
    PriorityID=forms.ChoiceField(choices=[(None, '---------'),(1,'Urgent'), (2, 'Important'), (3, 'Normal'), (4, 'Low')])
   

    
    