from django.shortcuts import render
# Create your views here.

def index_gender(request):
    return render(request, 'genders/index.html')

def index_user(request):
    return render(request, 'users/index.html')
