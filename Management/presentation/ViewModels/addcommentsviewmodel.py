from django import  forms


class CommentsForm(forms.Form):
    content=forms.CharField(max_length=255)