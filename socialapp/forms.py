from django import forms

class RegForm(forms.Form):
          name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Username","id":"form_name"}))
          email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email","id":"form_name"}))
          number=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter number","id":"form_name"}))
          password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))


class LoginForm(forms.Form):
    

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username","id":"form_name"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))

class NotesForm(forms.Form):
           contents=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter notes","id":"form_name"}))
