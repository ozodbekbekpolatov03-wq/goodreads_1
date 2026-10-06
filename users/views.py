from multiprocessing import AuthenticationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.template import context
from django.views import View
from django.contrib.auth.models import User
from users.forms import UserCreateForm, UserUpdateForms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# from xml.utils import is_valid_name

# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'users/register.html')
#     def post(self, request):
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user=User.objects.create(
#             username=username, 
#             first_name=first_name, 
#             last_name=last_name, 
#             email=email, 
#             password=password
#             )
#         user.set_password(password) # parolni shifrlash
#         user.save()
#         return redirect('login')
#     # Bunda user yaratilmaydi.

# class RegisterView(View):
#     def get(self, request):
#         create_form = UserCreateForm
#         context={
#             'form': create_form
#         }
#         return render(request, 'users/register.html', context)
#     def post(self, request):
#         create_form = UserCreateForm(data=request.POST)
#         if create_form.is_valid():
#             username = create_form.cleaned_data.get('username')
#             first_name = create_form.cleaned_data.get('first_name')
#             last_name = create_form.cleaned_data.get('last_name')
#             email = create_form.cleaned_data.get('email')
#             password = create_form.cleaned_data.get('password')
#             user=User.objects.create(
#                 username=username, 
#                 first_name=first_name, 
#                 last_name=last_name, 
#                 email=email, 
#                 password=password
#                 )
#             user.set_password(password) # parolni shifrlash
#             user.save()
#             return redirect('login')
#         else:
#             context={
#                 'form': create_form
#             }
#             return render(request, 'users/register.html', context)

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context={
            'form': create_form
        }
        return render(request, 'users/register.html', context)
    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')
        else:
            context={
                'form': create_form
            }
            return render(request, 'users/register.html', context)

class LoginView(View):
    def get(self, request):
        login_form=AuthenticationForm()
        context={
            'login_form':login_form
        }
        return render(request, 'users/login.html', context)
    
    # def post(self, request):
    #     print( request.POST['username'], request.POST['password'])
    #     login_form=UserLoginForm()
    #     context={
    #         'login_form':login_form
    #     }
    #     return render(request, 'users/login.html', context)

    def post(self,request):
        login_form=AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            messages.success(request, f'Xush kelibsiz, {user.username}!')
            return redirect('books:list')
        else:
            context={
                'login_form': login_form
            }
            return render(request, 'users/login.html', context)

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context={
            'user': request.user
        }
        return render(request, 'users/profile.html', context)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Siz tizimdan muvaffaqiyatli chiqdingiz.')
        return redirect('landing_page')

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self,request):
        user_update_forms=UserUpdateForms(instance=request.user)
        context={
            'form':user_update_forms
        }
        return render (request, 'users/profile_edit.html', context)
    
    def post(self,request):
        user_update_forms=UserUpdateForms( instance=request.user, data=request.POST)
        if user_update_forms.is_valid():
            user_update_forms.save()
            messages.success(request,"Sizning profilingiz movfaqyatli o'zgartrildi")
            return redirect('users:profile')
        context={
            'form':user_update_forms
        }
        return render (request, 'users/profile_edit.html', context)