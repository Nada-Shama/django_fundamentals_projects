from django.shortcuts import render, redirect
import random 

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100) 
    
    number = request.session['number'] 
    context = {
        'message': '',
        'bgcolor': 'white'
    }
    
    if request.method == 'POST':   
        guess = int(request.POST['guess'])

        if guess < number:
            context = {
                'message': 'Too Low!',
                'bgcolor': 'red'
            }
        elif guess > number:
            context = {
                'message': 'Too High!',
                'bgcolor': 'red'
            }
        elif guess == number:
            context = {
                'message': 'Correct Answer!',
                'bgcolor': 'green'
            }

    return render(request, 'index.html', context)

def reset(request):
    request.session.flush()  
    return redirect('/')
