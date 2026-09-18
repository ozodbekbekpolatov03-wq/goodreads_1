from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')
    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
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
    # Bunda user yaratilmaydi.
 

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
# Create your views here.
