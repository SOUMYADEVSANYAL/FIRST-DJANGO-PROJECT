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
            if (char =='\n'):
                analyzed = analyzed+"\n"
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
    
    elif(ana == "4"):
        analyzed=''
        for char in textvar:
            analyzed=analyzed+char.upper()
        params = {'purpose':'After capitalisation', 'result': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(ana == "5"):
        analyzed=''
        for char in textvar:
            analyzed=analyzed+char.lower()
        params = {'purpose':'Changed to lowercase', 'result': analyzed}
        return render(request, 'analyze.html', params)

    elif(ana == "6"):
        analyzed = ''
        for char in textvar:
            if (char == '\n'):
                analyzed=analyzed+' '
                continue
            analyzed=analyzed+char
        params = {'purpose':'Merged in one line', 'result': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")