from django.shortcuts import render , redirect
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm , ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    #success_url = reverse_lazy('login')
    def get_success_url(self) -> str:
        login(self.request , self.object)
        return reverse_lazy('Projects_list')



@login_required  #because request.user is available when logged in , we did this to get redirected to login page if not logged-in to avoid an error  
def EditProfile(request):
    
    if request.method =='POST':
        form = ProfileForm(request.POST , instance = request.user)  #it is available when logged in
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else : 
        form = ProfileForm(instance = request.user)  #it is available when logged in
        return render(request , 'profile.html' ,{'form' :form })
    