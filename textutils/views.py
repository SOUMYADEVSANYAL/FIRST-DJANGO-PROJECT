# Soumyadev Sanyal made this file.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    textvar =  request.GET.get('text','No Text')
    ana = request.GET.get('ana', '0')
    if (ana == "1"):
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in textvar:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'After removing punctuations', 'result': analyzed}
        return render(request, 'analyze.html', params)

    elif(ana == "2"):
        analyzed = ''
        for char in textvar:
            if (char == ' '):
                continue
            analyzed=analyzed+char
        params = {'purpose':'After removing spaces', 'result': analyzed}
        return render(request, 'analyze.html', params)

    elif(ana == "3"):
        length=len(textvar)
        params = {'purpose':'Number of characters', 'result': length}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")