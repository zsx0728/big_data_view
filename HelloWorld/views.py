from django.http import HttpResponse
from django.shortcuts import render
from . import show1db
 
def hello(request):
    return HttpResponse("Hello world ! ")

def show(request):
    #value = {'complete':'199'}
    value = {'complete': show1db.completedb(), 'plan': show1db.plandb(), 'incomplete' : show1db.plandb() - show1db.completedb(), 'complete_percentage' : round(show1db.completedb()*100 / show1db.plandb(),2)}
    return render(request, 'index.html', {"value":value})
