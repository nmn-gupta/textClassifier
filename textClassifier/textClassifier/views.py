from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def translate(request):
    input_text = request.POST.get('text', 'default')
