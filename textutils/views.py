# Soumyadev Sanyal made this file.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    textvar =  request.POST.get('text','No Text')
    ana1 = request.POST.get('ana1', '0')
    ana2 = request.POST.get('ana2', '0')
    ana3 = request.POST.get('ana3', '0')
    ana4 = request.POST.get('ana4', '0')
    ana5 = request.POST.get('ana5', '0')
    ana6 = request.POST.get('ana6', '0')
    counted="Not counted"
    if (ana1 == "1"):
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in textvar:
            if (char =='\n'):
                analyzed = analyzed+"\n"
            if char not in punctuations:
                analyzed = analyzed + char
        textvar=analyzed
        # params = {'purpose':'After removing punctuations', 'result': analyzed}
        # return render(request, 'analyze.html', params)

    if(ana2 == "1"):
        analyzed = ''
        for char in textvar:
            if (char == ' '):
                continue
            analyzed=analyzed+char
        textvar=analyzed
        # params = {'purpose':'After removing spaces', 'result': analyzed}
        # return render(request, 'analyze.html', params)

    if(ana3 == "1"):
        length=len(textvar)
        counted= str(length)
        # params = {'purpose':'Number of characters', 'result': length}
        # return render(request,'analyze.html',params)
    
    if(ana4 == "1"):
        analyzed=''
        for char in textvar:
            analyzed=analyzed+char.upper()
        textvar=analyzed
        # params = {'purpose':'After capitalisation', 'result': analyzed}
        # return render(request, 'analyze.html', params)
    
    if(ana5 == "1"):
        analyzed=''
        for char in textvar:
            analyzed=analyzed+char.lower()
        textvar=analyzed
        # params = {'purpose':'Changed to lowercase', 'result': analyzed}
        # return render(request, 'analyze.html', params)

    if(ana6 == "1"):
        analyzed = ''
        for char in textvar:
            if (char != '\n' and char != '\r'):
                analyzed=analyzed+char
            else:
                analyzed=analyzed+' '
        textvar=analyzed
        # params = {'purpose':'Final result is:', 'result': analyzed, 'count': counted}
        # return render(request, 'analyze.html', params)

    if(ana1==ana2==ana3==ana4==ana5==ana6==0):
        return HttpResponse("Error")
    
    params = {'purpose':'Final result is:', 'result': textvar, 'count': counted}
    return render(request, 'analyze.html', params)