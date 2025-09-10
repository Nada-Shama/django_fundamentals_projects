from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')   

def result(request):
    if request.method == "POST":
        name = request.POST.get('user_name')
        dojo = request.POST.get('dojo')
        language = request.POST.get('language')
        comment = request.POST.get('comment')
        context = {
            'name': name,
            'dojo': dojo,
            'language': language,
            'comment': comment,
        }
        return render(request, 'result.html', context)
    else:
        return redirect('/')
