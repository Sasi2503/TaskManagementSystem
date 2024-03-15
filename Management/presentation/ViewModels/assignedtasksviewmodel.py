from datetime import date
from django import forms
from Management.DAL.Entities.Users import Users

class assignedForm(forms.Form):
    AssignedTo = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': "form-control"}))
    PriorityID = forms.ChoiceField(choices=[(None, '---------'),(1,'Urgent'), (2, 'Important'), (3, 'Normal'), (4, 'Low')])
    Status = forms.ChoiceField(choices=[(None, '---------'),(1,'Not Started'), (2, 'In Progress'), (3,'Completed')])
    DueDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))

    def __init__(self, *args, **kwargs):
        super(assignedForm, self).__init__(*args, **kwargs)
        registered_users = Users.objects.all()
        user_choices = [(user.UserID, user.firstname +' '+ user.lastname) for user in registered_users]
        self.fields['AssignedTo'].choices = user_choices
