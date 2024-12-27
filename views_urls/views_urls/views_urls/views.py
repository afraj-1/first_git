from django.shortcuts import render
from . import mlm
def home(request):
    return render(request, 'index.html')

def result(request):
    user = request.GET['user']
    user = mlm.mult(user)
    return render(request, 'result.html',{'user':user})