from django import forms
from.models import Members

# Creating classes in the forms page
class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['fname','lname','email','age']

