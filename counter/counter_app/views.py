from django.shortcuts import render,redirect

def index(request):
    if 'count' in request.session:     
        request.session['count'] += 1
    else:
        request.session['count'] = 1 

    context = {
        'count': request.session['count']
    }
    return render(request, 'index.html', context)


def destroy_session(request):
    request.session['count']=0
    context = {
        'count': request.session['count']
    }

    return redirect('/',context)

