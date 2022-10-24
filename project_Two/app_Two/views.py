from django.shortcuts import render
from app_Two.models import User
from app_Two.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'app_Two/index.html')

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return index(request)
        else:
            print("ERROR FORM IS INVALID")
            
    return render(request,'app_Two/users.html', {'form': form})
