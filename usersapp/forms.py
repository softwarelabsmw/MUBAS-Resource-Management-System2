from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    # Validate email
    def clean_email(self):
        mubasmail = "@mubas.ac.mw"
        cemail = self.cleaned_data['email']
        if mubasmail not in cemail:
            raise forms.ValidationError("Enter a correct MUBAS email address e.g., name@mubas.ac.mw")
        return cemail

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('reg_no', 'first_name', 'last_name', 'email', 'phone', 
                                                 'gender','department', 'user_type', 'photo', )
class UserChangeForm(UserChangeForm):
    def clean_email(self):
        mubasmail = "@mubas.ac.mw"
        cemail = self.cleaned_data['email']
        if mubasmail not in cemail:
            raise forms.ValidationError("Use your MUBAS email address e.g., name@mubas.ac.mw")
        return cemail

    class Meta:
        model = User
        fields = ['phone', 'department', 'photo']
        