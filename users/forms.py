from django import forms
from django.contrib.auth.models import User

# class UserCreateForm(forms.Form):
#     username= forms.CharField(max_length=150)
#     email= forms.EmailField()
#     first_name= forms.CharField(max_length=150)
#     last_name= forms.CharField(max_length=150)  
#     password= forms.CharField(max_length=128)
#     def save(self):
#         username=self.cleaned_data['username']
#         email=self.cleaned_data['email']
#         first_name=self.cleaned_data['first_name']
#         last_name=self.cleaned_data['last_name']
#         password=self.cleaned_data['password']
#         user=User.objects.create(
#             username=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save()
#         return user
class UserCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email', 'first_name', 'last_name', 'password']
        
    def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

# class UserLoginForm(forms.Form):
#     username=forms.CharField(max_length=150)
#     password=forms.CharField(max_length=128)
