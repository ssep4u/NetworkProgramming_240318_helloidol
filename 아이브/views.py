from django.shortcuts import render

def show_유진(request):
    return render(request, '아이브/유진.html')


def show_원영(request):
    return render(request, '아이브/원영.html')
