from django.shortcuts import render
from basic_app.forms import UserForm,ProfileForm
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered = False
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(userform.errors, profileform.errors)
    else:
        userform =UserForm()
        profileform = ProfileForm()
    return render(request,'basic_app/registration.html',{'user_form':userform,'profile_form':profileform,'registered':registered})
