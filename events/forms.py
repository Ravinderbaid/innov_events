from django import forms
from events.models import Events,User
from django.contrib.auth.forms import UserCreationForm



class MyRegistrationForm(UserCreationForm):


    GENDER_CHOICES=(
        (0,'Male'),
        (1,'Female')
    )
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required=True)
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()

        return user
