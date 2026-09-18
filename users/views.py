from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from users.forms import UserCreateForm
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
            username = create_form.cleaned_data.get('username')
            first_name = create_form.cleaned_data.get('first_name')
            last_name = create_form.cleaned_data.get('last_name')
            email = create_form.cleaned_data.get('email')
            password = create_form.cleaned_data.get('password')
            user=User.objects.create(
                username=username, 
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                password=password
                )
            user.set_password(password) # parolni shifrlash
            user.save()
            return redirect('login')
        else:
            context={
                'form': create_form
            }
            return render(request, 'users/register.html', context)

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
# Create your views here.
