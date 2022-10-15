from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(required=True, max_length=20,min_length=2,label="",strip=True)
    #task_up = forms.CharField(required=True, max_length=20,min_length=2,label="",strip=True)
