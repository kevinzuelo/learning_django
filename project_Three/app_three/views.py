from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_content': 'Hello from the third app!'}
    return render(request, 'app_three/index.html', context=my_dict)
