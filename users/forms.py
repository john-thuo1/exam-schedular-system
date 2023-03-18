'''
UserRegisterForm is a form for user registration and inherits from UserCreationForm, which is a built-in form provided by Django for creating new users. 
It adds an email field to the form and specifies which fields from the User model should be used.
'''


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import Profile


# The default usercreationform provides only username and password fields.
# But for our case, we need to add other fields hence creating a new form that extends the built in UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

'''
form for updating user information and inherits from forms.ModelForm. 
It adds an email field to the form and specifies which fields from the User model should be used.
'''

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


'''
form for updating user profile information and inherits from forms.ModelForm. 
It specifies that all fields from the Profile model should be used in the form.
'''
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
