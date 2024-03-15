from django import forms
from datetime import date

class UpdateTaskForm(forms.Form):
    Title=forms.CharField(max_length=100)
    Description = forms.CharField(widget=forms.Textarea,required=False)

class UpdateStatusForm(forms.Form):
    Status=forms.ChoiceField(choices=[(None, '---------'),(1,'Not Started'), (2, 'In Progress'), (3,'Completed')])
    Priority = forms.ChoiceField(choices=[(None, '---------'),(1,'Urgent'), (2, 'Important'), (3, 'Normal'), (4, 'Low')])
    DueDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))

