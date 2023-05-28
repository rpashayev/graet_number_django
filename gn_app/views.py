from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def start(request):
    if 'num' not in request.session:
        request.session['num'] = randint(1, 100)
        request.session['try'] = 0
        request.session['tries_left'] = 5
    else:
        request.session['try'] += 1
        request.session['tries_left'] -= 1    
        
    return render(request, 'index.html')

def guess(request):
    request.session['guess'] = int(request.POST['guess_number'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')